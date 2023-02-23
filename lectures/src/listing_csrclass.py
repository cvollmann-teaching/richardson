class csr_matrix:
    """
    Compressed Sparse Row matrix

    This can be instantiated via:
        csr_matrix((data, indices, indptr), [shape=(m,n)])

    Attributes
    ----------
    data : list
        CSR format data array of the matrix
    indices : list
         CSR format index array of the matrix
    indptr : list
         CSR format index pointer array of the matrix
    shape : 2-tuple
        Shape of the matrix, optional

    Examples
    --------
    >>>
    ....


    """
    def __init__(self, csrTuple, shape=None):
        _data, _indices, _indptr = csrTuple
        if shape:
            self.shape = shape
        self.data = _data
        self.indices = _indices
        self.indptr = _indptr

    def toarray():
        pass

    def __matmul__(a,b):
        pass

