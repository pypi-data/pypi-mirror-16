# CHOLMOD wrapper for scikits.sparse

# Copyright (C) 2009 Nathaniel Smith <njs@pobox.com>
# Copyright (C) 2016 Antony Lee <anntzer.lee@gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# - Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
# - Redistributions in binary form must reproduce the above
#   copyright notice, this list of conditions and the following
#   disclaimer in the documentation and/or other materials
#   provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
# TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
# TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
# THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

#cython: binding = True
#cython: language_level = 3
#distutils: include_dirs = NP_GET_INCLUDE /usr/include/suitesparse
#distutils: libraries = cholmod

cimport numpy as np

import warnings
import numpy as np
from scipy import sparse

np.import_array()

cdef extern from "numpy/arrayobject.h":
    void PyArray_ENABLEFLAGS(np.ndarray arr, int flags)

cdef extern from "cholmod.h":
    cdef enum:
        CHOLMOD_INT
        CHOLMOD_PATTERN, CHOLMOD_REAL, CHOLMOD_COMPLEX
        CHOLMOD_DOUBLE
        CHOLMOD_AUTO, CHOLMOD_SIMPLICIAL, CHOLMOD_SUPERNODAL
        CHOLMOD_OK, CHOLMOD_NOT_POSDEF
        CHOLMOD_A, CHOLMOD_LDLt, CHOLMOD_LD, CHOLMOD_DLt, CHOLMOD_L
        CHOLMOD_Lt, CHOLMOD_D, CHOLMOD_P, CHOLMOD_Pt

    ctypedef struct cholmod_common:
        int supernodal
        int status
        int print
        void (*error_handler)(int status, const char * file, int line, const char * msg)

    int cholmod_start(cholmod_common *) except? 0
    int cholmod_finish(cholmod_common *) except? 0
    int cholmod_check_common(cholmod_common *) except? 0
    int cholmod_print_common(char *, cholmod_common *) except? 0

    ctypedef struct cholmod_sparse:
        size_t nrow, ncol, nzmax
        void * p # column pointers
        void * i # row indices
        void * x
        int stype # 0 = regular, >0 = upper triangular, <0 = lower triangular
        int itype # type of p, i, nz
        int xtype
        int dtype
        int sorted
        int packed

    int cholmod_free_sparse(cholmod_sparse **, cholmod_common *) except? 0
    int cholmod_check_sparse(cholmod_sparse *, cholmod_common *) except? 0
    int cholmod_print_sparse(cholmod_sparse *, char *, cholmod_common *) except? 0

    ctypedef struct cholmod_dense:
        size_t nrow, ncol, nzmax
        size_t d
        void * x
        int xtype, dtype

    int cholmod_free_dense(cholmod_dense **, cholmod_common *) except? 0
    int cholmod_check_dense(cholmod_dense *, cholmod_common *) except? 0
    int cholmod_print_dense(cholmod_dense *, char *, cholmod_common *) except? 0

    ctypedef struct cholmod_factor:
        size_t n
        void * Perm
        int itype
        int xtype
        int is_ll, is_super, is_monotonic
        size_t xsize, nzmax, nsuper
        void * x
        void * p
        void * super_ "super"
        void * pi
        void * px
    int cholmod_free_factor(cholmod_factor **, cholmod_common *) except? 0
    cholmod_factor * cholmod_copy_factor(cholmod_factor *, cholmod_common *) except? NULL

    cholmod_factor * cholmod_analyze(cholmod_sparse *, cholmod_common *) except? NULL
    int cholmod_factorize_p(cholmod_sparse *, double beta[2],
                            int * fset, size_t fsize,
                            cholmod_factor *,
                            cholmod_common *) except? 0

    cholmod_sparse * cholmod_submatrix(cholmod_sparse *,
                                       int * rset, int rsize,
                                       int * cset, int csize,
                                       int values, int sorted,
                                       cholmod_common *) except? NULL
    int cholmod_updown(int update, cholmod_sparse *, cholmod_factor *,
                       cholmod_common *) except? 0

    cholmod_dense * cholmod_solve(int, cholmod_factor *,
                                  cholmod_dense *, cholmod_common *) except? NULL
    cholmod_sparse * cholmod_spsolve(int, cholmod_factor *,
                                     cholmod_sparse *, cholmod_common *) except? NULL

    int cholmod_change_factor(int to_xtype, int to_ll, int to_super,
                              int to_packed, int to_monotonic,
                              cholmod_factor *, cholmod_common *) except? 0
    cholmod_sparse * cholmod_factor_to_sparse(cholmod_factor *,
                                              cholmod_common *) except? NULL

cdef class Common
cdef class Factor

class CholmodError(Exception):
    pass

class CholmodWarning(UserWarning):
    pass

class CholmodTypeConversionWarning(
        CholmodWarning, sparse.SparseEfficiencyWarning):
    pass

cdef int _integer_typenum = np.NPY_INT32
cdef object _integer_py_dtype = np.dtype(np.int32)
assert sizeof(int) == _integer_py_dtype.itemsize == 4

cdef int _real_typenum = np.NPY_FLOAT64
cdef object _real_py_dtype = np.dtype(np.float64)
assert sizeof(double) == _real_py_dtype.itemsize == 8

cdef int _complex_typenum = np.NPY_COMPLEX128
cdef object _complex_py_dtype = np.dtype(np.complex128)
assert 2 * sizeof(double) == _complex_py_dtype.itemsize == 16

cdef _require_1d_integer(a):
    if a.dtype.itemsize != _integer_py_dtype.itemsize:
        warnings.warn("array contains %s bit integers; "
                      "this will be slower than using %s bit integers"
                      % (a.dtype.itemsize * 8,
                         _integer_py_dtype.itemsize * 8),
                      CholmodTypeConversionWarning)
    a = np.ascontiguousarray(a, dtype=_integer_py_dtype)
    assert a.ndim == 1
    return a

##########
# Cholmod -> Python conversion:
##########

cdef int _np_typenum_for(int xtype):
    if xtype == CHOLMOD_COMPLEX:
        return _complex_typenum
    elif xtype == CHOLMOD_REAL:
        return _real_typenum
    else:
        raise CholmodError("cholmod->numpy type conversion failed")

cdef type _np_dtype_for(int xtype):
    return np.PyArray_TypeObjectFromType(_np_typenum_for(xtype))

cdef class _SparseCleanup:
    cdef cholmod_sparse * _sparse
    cdef Common _common
    def __dealloc__(self):
        cholmod_free_sparse(&self._sparse, &self._common._common)

cdef _py_sparse(cholmod_sparse * m, Common common):
    """Build a scipy.sparse.csc_matrix that's a view onto m, with a 'base' with
    appropriate destructor. 'm' must have been allocated by cholmod."""

    # This is a little tricky -- we build 3 arrays, views on each part of the
    # cholmod_dense object -- and they all have the same _SparseCleanup object
    # as base. So none of them will be deallocated until they have all become
    # unused. Then those are built into a csc_matrix.

    assert m is not NULL
    assert common is not None
    # Construct cleaner first, so even if we later raise an exception we still
    # fulfill the contract that we will take care of cleanup:
    cdef _SparseCleanup cleaner = _SparseCleanup()
    cleaner._sparse = m
    cleaner._common = common
    assert m.itype == CHOLMOD_INT

    cdef np.ndarray indptr = np.PyArray_SimpleNewFromData(
        1, [m.ncol + 1], _integer_typenum, m.p)
    PyArray_ENABLEFLAGS(indptr, np.NPY_WRITEABLE)
    np.set_array_base(indptr, cleaner)
    cdef np.ndarray indices = np.PyArray_SimpleNewFromData(
        1, [m.nzmax], _integer_typenum, m.i)
    PyArray_ENABLEFLAGS(indices, np.NPY_WRITEABLE)
    np.set_array_base(indices, cleaner)
    cdef np.ndarray data = np.PyArray_SimpleNewFromData(
        1, [m.nzmax], _np_typenum_for(m.xtype), m.x)
    PyArray_ENABLEFLAGS(data, np.NPY_WRITEABLE)
    np.set_array_base(data, cleaner)

    return sparse.csc_matrix((data, indices, indptr), shape=(m.nrow, m.ncol))

cdef class _DenseCleanup:
    cdef cholmod_dense * _dense
    cdef Common _common
    def __dealloc__(self):
        cholmod_free_dense(&self._dense, &self._common._common)

cdef _py_dense(cholmod_dense * m, Common common):
    """Build an ndarray that's a view onto m, with a 'base' with appropriate
    destructor. 'm' must have been allocated by cholmod."""

    assert m is not NULL
    assert common is not None
    # Construct cleaner first, so even if we later raise an exception we still
    # fulfill the contract that we will take care of cleanup:
    cdef _DenseCleanup cleaner = _DenseCleanup()
    cleaner._dense = m
    cleaner._common = common

    cdef np.ndarray out = np.PyArray_SimpleNewFromData(
        1, [m.ncol * m.nrow], _np_typenum_for(m.xtype), m.x).reshape((m.ncol, m.nrow)).T
    PyArray_ENABLEFLAGS(out, np.NPY_WRITEABLE)
    np.set_array_base(out, cleaner)

    return out

cdef void _error_handler(
        int status, const char * file, int line, const char * msg) except * with gil:
    if status == CHOLMOD_OK:
        return
    full_msg = "%s:%s: %s (code %s)" % (file, line, msg, status)
    if status > 0:
        # Warning:
        warnings.warn(full_msg, CholmodWarning)
    else:
        raise CholmodError(full_msg)

cdef class Common:
    cdef cholmod_common _common
    cdef int _complex
    cdef int _xtype

    def __cinit__(self, _complex):
        self._complex = _complex
        if self._complex:
            self._xtype = CHOLMOD_COMPLEX
        else:
            self._xtype = CHOLMOD_REAL
        cholmod_start(&self._common)
        self._common.print = 0
        self._common.error_handler = (
            <void (*)(int, const char *, int, const char *)>_error_handler)

    def __dealloc__(self):
        cholmod_finish(&self._common)

    # Debugging:
    def _print(self):
        print(cholmod_check_common(&self._common))
        name = repr(self)
        return cholmod_print_common(name, &self._common)

    def _print_sparse(self, name, symmetric, matrix):
        cdef cholmod_sparse m
        cdef object ref = self._init_view_sparse(&m, matrix, symmetric)
        print(cholmod_check_sparse(&m, &self._common))
        return cholmod_print_sparse(&m, name, &self._common)

    def _print_dense(self, name, matrix):
        cdef cholmod_dense m
        cdef object ref = self._init_view_dense(&m, matrix)
        print(cholmod_check_dense(&m, &self._common))
        return cholmod_print_dense(&m, name, &self._common)

    ##########
    # Python -> Cholmod conversion:
    ##########
    cdef np.ndarray _cast(self, np.ndarray arr):
        if not issubclass(arr.dtype.type, np.number):
            raise CholmodError("non-numeric dtype %s" % (arr.dtype,))
        if self._complex:
            # All numeric types can be upcast to complex:
            return np.asfortranarray(arr, dtype=_complex_py_dtype)
        else:
            # Refuse to downcast complex types to real:
            if issubclass(arr.dtype.type, np.complexfloating):
                raise CholmodError("inconsistent use of complex array")
            else:
                return np.asfortranarray(arr, dtype=_real_py_dtype)

    # Some memory allocated for the init'd sparse matrix is refcounted by the
    # returned object; do not let it be garbage collected as long as you want
    # to use the matrix.
    cdef object _init_view_sparse(self, cholmod_sparse *out, m, symmetric):
        if not sparse.isspmatrix_csc(m):
            warnings.warn("converting matrix of class %s to CSC format"
                          % (m.__class__.__name__,),
                          CholmodTypeConversionWarning)
            m = m.tocsc()
        if symmetric and m.shape[0] != m.shape[1]:
            raise CholmodError("supposedly symmetric matrix is not square!")
        m.sort_indices()
        cdef np.ndarray indptr = _require_1d_integer(m.indptr)
        cdef np.ndarray indices = _require_1d_integer(m.indices)
        cdef np.ndarray data = self._cast(m.data)
        out.nrow, out.ncol = m.shape
        out.nzmax = m.nnz
        out.p = indptr.data
        out.i = indices.data
        out.x = data.data
        if symmetric:
            out.stype = -1
        else:
            out.stype = 0
        out.itype = CHOLMOD_INT
        out.dtype = CHOLMOD_DOUBLE
        out.xtype = self._xtype
        out.sorted = 1
        out.packed = 1
        return m, indptr, indices, data

    # Some memory allocated for the init'd dense matrix is refcounted by the
    # returned object; do not let it be garbage collected as long as you want
    # to use the matrix.
    cdef object _init_view_dense(self, cholmod_dense *out, np.ndarray m):
        if m.ndim != 2:
            raise CholmodError("array has %s dimensions (expected 2)" % m.ndim)
        m = self._cast(m)
        out.nrow = m.shape[0]
        out.ncol = m.shape[1]
        out.nzmax = m.size
        out.d = m.strides[1] // m.itemsize
        out.x = m.data
        out.dtype = CHOLMOD_DOUBLE
        out.xtype = self._xtype
        return m

cdef object factor_secret_handshake = object()

cdef class Factor:
    """This class represents a Cholesky decomposition with a particular
    fill-reducing permutation. It cannot be instantiated directly; see
    :func:`analyze` and :func:`cholesky`, both of which return objects of type
    Factor.
    """

    cdef readonly Common _common
    cdef cholmod_factor * _factor

    def __init__(self, handshake):
        if handshake is not factor_secret_handshake:
            raise CholmodError("Factor may not be constructed directly; use analyze()")

    def __dealloc__(self):
        cholmod_free_factor(&self._factor, &self._common._common)

    def cholesky_inplace(self, A, beta=0):
        """Updates this Factor so that it represents the Cholesky
        decomposition of :math:`A + \\beta I`, rather than whatever it
        contained before.

        :math:`A` must have the same pattern of non-zeros as the matrix used
        to create this factor originally."""
        return self._cholesky_inplace(A, True, beta=beta)

    def cholesky_AAt_inplace(self, A, beta=0):
        """The same as :meth:`cholesky_inplace`, except it factors :math:`AA'
        + \\beta I` instead of :math:`A + \\beta I`."""
        return self._cholesky_inplace(A, False, beta=beta)

    def _cholesky_inplace(self, A, symmetric, beta=0, **kwargs):
        cdef cholmod_sparse c_A
        cdef object ref = self._common._init_view_sparse(&c_A, A, symmetric)
        cholmod_factorize_p(&c_A, [beta, 0], NULL, 0,
                            self._factor, &self._common._common)
        if self._common._common.status == CHOLMOD_NOT_POSDEF:
            raise CholmodError("Matrix is not positive definite")

    def _clone(self):
        cdef cholmod_factor * c_clone = cholmod_copy_factor(self._factor,
                                                            &self._common._common)
        assert c_clone
        cdef Factor clone = Factor(factor_secret_handshake)
        clone._common = self._common
        clone._factor = c_clone
        return clone

    def cholesky(self, A, beta=0):
        """The same as :meth:`cholesky_inplace` except that it first creates
        a copy of the current :class:`Factor` and modifes the copy.

        :returns: The new :class:`Factor` object."""
        clone = self._clone()
        clone.cholesky_inplace(A, beta=beta)
        return clone

    def cholesky_AAt(self, A, beta=0):
        """The same as :meth:`cholesky_AAt_inplace` except that it first
        creates a copy of the current :class:`Factor` and modifes the copy.

        :returns: The new :class:`Factor` object."""
        clone = self._clone()
        clone.cholesky_AAt_inplace(A, beta=beta)
        return clone

    def update_inplace(self, C, bint subtract=False):
        """Incremental building of :math:`AA'` decompositions.

        Updates this factor so that instead of representing the decomposition
        of :math:`A` (:math:`AA'`), it computes the decomposition of
        :math:`A + CC'` (:math:`AA' + CC'`) for ``subtract=False`` which is the
        default, or :math:`A - CC'` (:math:`AA' - CC'`) for
        ``subtract=True``. This method does not require that the
        :class:`Factor` was created with :func:`cholesky_AAt`, though that
        is the common case.

        The usual use for this is to factor AA' when A has a large number of
        columns, or those columns become available incrementally. Instead of
        loading all of A into memory, one can load in 'strips' of columns and
        pass them to this method one at a time.

        Note that no fill-reduction analysis is done; whatever permutation was
        chosen by the initial call to :func:`analyze` will be used regardless
        of the pattern of non-zeros in C."""
        # permute C
        cdef cholmod_sparse c_C
        cdef object ref = self._common._init_view_sparse(&c_C, C, False)
        cdef cholmod_sparse * C_perm = cholmod_submatrix(
            &c_C, <int *> self._factor.Perm, self._factor.n, NULL, -1, True, True,
            &self._common._common)
        assert C_perm
        try:
            cholmod_updown(not subtract, C_perm, self._factor,
                           &self._common._common)
        finally:
            cholmod_free_sparse(&C_perm, &self._common._common)

    # Everything below here will fail for matrices that were only analyzed,
    # not factorized.
    def P(self):
        """Returns the fill-reducing permutation P, as a vector of indices.

        The decomposition :math:`LL'` or :math:`LDL'` is of::

          A[P[:, np.newaxis], P[np.newaxis, :]]

        (or similar for AA')."""
        if self._factor.Perm is NULL:
            raise CholmodError("you must analyze a matrix first")
        assert self._factor.itype == CHOLMOD_INT

        cdef np.ndarray out = np.PyArray_SimpleNewFromData(
            1, [self._factor.n], _integer_typenum, self._factor.Perm)
        np.set_array_base(out, self)

        return out

    def _ensure_L_or_LD_inplace(self, want_L):
        # In CHOLMOD, supernodal factorizations are always LL'. If we request
        # to change to a supernodal LDL' factorization, cholmod_change_factor
        # will silently do nothing! So we can only stay supernodal when LL' is
        # requested:
        want_super = self._factor.is_super and want_L
        cholmod_change_factor(self._factor.xtype,
                              want_L, # to_ll
                              want_super,
                              True, # to_packed
                              self._factor.is_monotonic,
                              self._factor,
                              &self._common._common)
        assert bool(self._factor.is_ll) == want_L

    def _L_or_LD(self, want_L):
        cdef Factor f = self._clone()
        cdef cholmod_sparse * l
        f._ensure_L_or_LD_inplace(want_L)
        l = cholmod_factor_to_sparse(f._factor,
                                     &f._common._common)
        assert l
        return _py_sparse(l, self._common)

    def D(self):
        """Converts this factorization to the style

          .. math:: LDL' = PAP'

        or

          .. math:: LDL' = PAA'P'

        and then returns the diagonal matrix D *as a 1d vector*.

          .. note:: This method uses an efficient implementation that extracts
             the diagonal D directly from CHOLMOD's internal
             representation. It never makes a copy of the factor matrices, or
             actually converts a full `LL'` factorization into an `LDL'`
             factorization just to extract `D`.

        """

        if self._factor.xtype == CHOLMOD_PATTERN:
            raise CholmodError("cannot extract diagonal from a symbolic "
                               "factor; call a cholesky*() method first.")

        cdef np.ndarray x = np.PyArray_SimpleNewFromData(
            1, [self._factor.xsize if self._factor.is_super else self._factor.nzmax],
            _np_typenum_for(self._factor.xtype), self._factor.x)

        cdef size_t i
        cdef np.npy_intp n
        cdef int * super_ = <int *> self._factor.super_
        cdef int * pi = <int *> self._factor.pi
        cdef int * px = <int *> self._factor.px
        if self._factor.is_super:
            # This is a supernodal factorization, which is stored as a bunch
            # of dense, lower-triangular, column-major arrays packed into the
            # x vector. This is not documented in the CHOLMOD user-guide, or
            # anywhere else as far as I can tell; I got the details from
            # CVXOPT's C/cholmod.c.
            d = np.empty(self._factor.n, dtype=_np_dtype_for(self._factor.xtype))
            filled = 0
            for i in xrange(self._factor.nsuper):
                ncols = super_[i + 1] - super_[i]
                nrows = pi[i + 1] - pi[i]
                d[filled:filled + ncols] = x[px[i]
                                             :px[i] + nrows * ncols
                                             :nrows + 1]
                filled += ncols
        else:
            # This is a simplicial factorization, which is simply stored as a
            # sparse CSC matrix in x, p, i. We want the diagonal, which is
            # just the first entry in each column; p gives the offsets in x to
            # the beginning of each column.

            # The ->p array actually has n+1 entries, but only the first n
            # entries actually point to real columns (the last entry is a
            # sentinel), so we just create a view onto those:
            p = np.PyArray_SimpleNewFromData(
                1, [self._factor.n], _integer_typenum, self._factor.p)

            d = x[p]
        if self._factor.is_ll:
            return d ** 2
        else:
            return d

    def L(self):
        """If necessary, converts this factorization to the style

          .. math:: LL' = PAP'

        or

          .. math:: LL' = PAA'P'

        and then returns the sparse lower-triangular matrix L.

        .. warning:: The L matrix returned by this method and the one returned
           by :meth:`L_D` are different!
        """
        return self._L_or_LD(True)

    def LD(self):
        """If necessary, converts this factorization to the style

          .. math:: LDL' = PAP'

        or

          .. math:: LDL' = PAA'P'

        and then returns a sparse lower-triangular matrix "LD", which contains
        the D matrix on its diagonal, plus the below-diagonal part of L (the
        actual diagonal of L is all-ones).

        See :meth:`L_D` for a more convenient interface."""
        return self._L_or_LD(False)

    def L_D(self):
        """If necessary, converts this factorization to the style

          .. math:: LDL' = PAP'

        or

          .. math:: LDL' = PAA'P'

        and then returns the pair (L, D) where L is a sparse lower-triangular
        matrix and D is a sparse diagonal matrix.

        .. warning:: The L matrix returned by this method and the one returned
           by :meth:`L` are different!
        """
        ld = self.LD()
        l = sparse.tril(ld, -1) + sparse.eye(*ld.shape)
        d = sparse.dia_matrix((ld.diagonal(), [0]), shape=ld.shape)
        return (l, d)

    def solve_A(self, b):
        """Returns :math:`x`, where :math:`Ax = b` (or :math:`AA'x = b`, if
        you used :func:`cholesky_AAt`).

        :meth:`__call__` is an alias for this function, i.e., you can simply
        call the :class:`Factor` object like a function to solve :math:`Ax =
        b`."""
        return self._solve(b, CHOLMOD_A)

    def __call__(self, b):
        "Alias for :meth:`solve_A`."
        return self.solve_A(b)

    def solve_LDLt(self, b):
        """Returns :math:`x`, where :math:`LDL'x = b`.

        (This is different from :meth:`solve_A` because it does not correct
        for the fill-reducing permutation.)"""
        return self._solve(b, CHOLMOD_LDLt)

    def solve_LD(self, b):
        "Returns :math:`x`, where :math:`LDx = b`."
        self._ensure_L_or_LD_inplace(False)
        return self._solve(b, CHOLMOD_LD)

    def solve_DLt(self, b):
        "Returns :math:`x`, where :math:`DL'x = b`."
        self._ensure_L_or_LD_inplace(False)
        return self._solve(b, CHOLMOD_DLt)

    def solve_L(self, b):
        "Returns :math:`x`, where :math:`Lx = b`."
        self._ensure_L_or_LD_inplace(False)
        return self._solve(b, CHOLMOD_L)

    def solve_Lt(self, b):
        "Returns :math:`x`, where :math:`L'x = b`."
        self._ensure_L_or_LD_inplace(False)
        return self._solve(b, CHOLMOD_Lt)

    def solve_D(self, b):
        "Returns :math:`x`, where :math:`Dx = b`."
        return self._solve(b, CHOLMOD_D)

    # CHOLMOD API is quite confusing here -- unlike all the other solve
    # magic constants, CHOLMOD_P and CHOLMOD_Pt actually apply the matrix to b
    # rather than performing a matrix solve. Basically their names are
    # backwards... therefore let's call the functions `apply_P` and `apply_Pt`.
    def apply_P(self, b):
        "Returns :math:`x`, where :math:`x = Pb`."
        return self._solve(b, CHOLMOD_P)

    def apply_Pt(self, b):
        "Returns :math:`x`, where :math:`x = P'b`."
        return self._solve(b, CHOLMOD_Pt)

    def _solve(self, b, system):
        if sparse.issparse(b):
            return self._solve_sparse(b, system)
        else:
            return self._solve_dense(b, system)

    def _solve_sparse(self, b, system):
        cdef cholmod_sparse c_b
        cdef object ref = self._common._init_view_sparse(&c_b, b, False)
        cdef cholmod_sparse *out = cholmod_spsolve(
            system, self._factor, &c_b, &self._common._common)
        return _py_sparse(out, self._common)

    def _solve_dense(self, b, system):
        b = np.asarray(b)
        ndim = b.ndim
        if b.ndim == 1:
            b = b[:, np.newaxis]
        cdef cholmod_dense c_b
        cdef object ref = self._common._init_view_dense(&c_b, b)
        cdef cholmod_dense *out = cholmod_solve(
            system, self._factor, &c_b, &self._common._common)
        py_out = _py_dense(out, self._common)
        if ndim == 1:
            py_out = py_out[:, 0]
        return py_out

    def slogdet(self):
        """Computes the log-determinant of the matrix A, with the same API as
        :meth:`numpy.linalg.slogdet`.

        This returns a tuple `(sign, logdet)`, where `sign` is always the
        number 1.0 (because the determinant of a positive-definite matrix is
        always a positive real number), and `logdet` is the (natural)
        logarithm of the determinant of the matrix A.

        .. versionadded:: 0.2
        """
        return (1.0, self.logdet())

    def logdet(self):
        """Computes the (natural) log of the determinant of the matrix A.

        If `f` is a factor, then `f.logdet()` is equivalent to
        `np.sum(np.log(f.D()))`.

        .. versionadded:: 0.2
        """
        return np.sum(np.log(self.D()))

    def det(self):
        """Computes the determinant of the matrix A.

        Consider using :meth:`logdet` instead, for improved numerical
        stability. (In particular, determinants are often prone to problems
        with underflow or overflow.)

        .. versionadded:: 0.2
        """
        return np.exp(self.logdet())

    def inv(self):
        """Returns the inverse of the matrix A, as a sparse (CSC) matrix.

          .. warning:: For most purposes, it is better to use :meth:`solve`
             instead of computing the inverse explicitly. That is, the
             following two pieces of code produce identical results::

               x = f.solve(b)
               x = f.inv() * b  # DON'T DO THIS!

             But the first line is both faster and produces more accurate
             results.

        Sometimes, though, you really do need the inverse explicitly (e.g.,
        for calculating standard errors in least squares regression), so if
        that's your situation, here you go.

        .. versionadded:: 0.2
        """

        return self(sparse.eye(self._factor.n, self._factor.n,
                               dtype=_np_dtype_for(self._factor.xtype),
                               format="csc"))

def analyze(A, mode="auto"):
    """Computes the optimal fill-reducing permutation for the symmetric matrix
    A, but does *not* factor it (i.e., it performs a "symbolic Cholesky
    decomposition"). This function ignores the actual contents of the matrix
    A. All it cares about are (1) which entries are non-zero, and (2) whether
    A has real or complex type.

    :param A: The matrix to be analyzed.

    :param auto: Specifies which algorithm should be used to (eventually)
      compute the Cholesky decomposition -- one of "simplicial", "supernodal",
      or "auto". See the CHOLMOD documentation for details on how "auto" chooses
      the algorithm to be used.

    :returns: A :class:`Factor` object representing the analysis. Many
      operations on this object will fail, because it does not yet hold a full
      decomposition. Use :meth:`Factor.cholesky_inplace` (or similar) to
      actually factor a matrix.
    """
    return _analyze(A, True, mode=mode)

def analyze_AAt(A, mode="auto"):
    """Computes the optimal fill-reducing permutation for the symmetric matrix
    :math:`AA'`, but does *not* factor it (i.e., it performs a "symbolic
    Cholesky decomposition"). This function ignores the actual contents of the
    matrix A. All it cares about are (1) which entries are non-zero, and (2)
    whether A has real or complex type.

    :param A: The matrix to be analyzed.

    :param auto: Specifies which algorithm should be used to (eventually)
      compute the Cholesky decomposition -- one of "simplicial", "supernodal",
      or "auto". See the CHOLMOD documentation for details on how "auto" chooses
      the algorithm to be used.

    :returns: A :class:`Factor` object representing the analysis. Many
      operations on this object will fail, because it does not yet hold a full
      decomposition. Use :meth:`Factor.cholesky_AAt_inplace` (or similar) to
      actually factor a matrix.
    """
    return _analyze(A, False, mode=mode)

_modes = {
    "simplicial": CHOLMOD_SIMPLICIAL,
    "supernodal": CHOLMOD_SUPERNODAL,
    "auto": CHOLMOD_AUTO,
    }
def _analyze(A, symmetric, mode):
    cdef Common common = Common(issubclass(A.dtype.type, np.complexfloating))
    cdef cholmod_sparse c_A
    cdef object ref = common._init_view_sparse(&c_A, A, symmetric)
    if mode in _modes:
        common._common.supernodal = _modes[mode]
    else:
        raise CholmodError("Unknown mode '%s', must be one of %s" %
                           (mode, ", ".join(_modes.keys())))
    cdef cholmod_factor *c_f = cholmod_analyze(&c_A, &common._common)
    if c_f is NULL:
        raise CholmodError("Error in cholmod_analyze")
    cdef Factor f = Factor(factor_secret_handshake)
    f._common = common
    f._factor = c_f
    return f

def cholesky(A, beta=0, mode="auto"):
    """Computes the fill-reducing Cholesky decomposition of

      .. math:: A + \\beta I

    where ``A`` is a sparse, symmetric, positive-definite matrix, preferably
    in CSC format, and ``beta`` is any real scalar (usually 0 or 1). (And
    :math:`I` denotes the identity matrix.)

    Only the lower triangular part of ``A`` is used.

    ``mode`` is passed to :func:`analyze`.

    :returns: A :class:`Factor` object represented the decomposition.
    """
    return _cholesky(A, True, beta=beta, mode=mode)

def cholesky_AAt(A, beta=0, mode="auto"):
    """Computes the fill-reducing Cholesky decomposition of

      .. math:: AA' + \\beta I

    where ``A`` is a sparse matrix, preferably in CSC format, and ``beta`` is
    any real scalar (usually 0 or 1). (And :math:`I` denotes the identity
    matrix.)

    Note that if you are solving a conventional least-squares problem, you
    will need to transpose your matrix before calling this function, and
    therefore it will be somewhat more efficient to construct your matrix in
    CSR format (so that its transpose will be in CSC format).

    ``mode`` is passed to :func:`analyze_AAt`.

    :returns: A :class:`Factor` object represented the decomposition.
    """
    return _cholesky(A, False, beta=beta, mode=mode)

def _cholesky(A, symmetric, beta, mode):
    f = _analyze(A, symmetric, mode=mode)
    f._cholesky_inplace(A, symmetric, beta=beta)
    return f

__all__ = ["analyze", "analyze_AAt", "cholesky", "cholesky_AAt"]
