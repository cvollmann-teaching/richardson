"""
Just based on built-in types and functions, this module provides data types for
vectors and csr-matrices as well as level 1 + 2 matrix vector operations to perform basic
linear algebra computations.
"""


# data types
class vector(list):
    """
    class to provide level 1 vector operations
    """

    def __add__(self, other):
        return vector([other_i + self_i for other_i, self_i in zip(other, self)])

    def __sub__(self, other):
        return vector([self_i - other_i for other_i, self_i in zip(other, self)])

    def __matmul__(self, other):
        if not isinstance(other, (tuple, list)):
            raise ValueError("use vector like types")
        return sum([other_i * self_i for other_i, self_i in zip(other, self)])

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise ValueError("use scalar types")
        return vector([other * self_i for self_i in self])

    def __rmul__(self, other):
        return self.__mul__(other)


class csr_matrix:
    """
    CSR matrix class
    """

    def __init__(self, csr_tuple, shape=None):
        _data, _indices, _indptr = csr_tuple
        self.data = _data
        self.indices = _indices
        self.indptr = _indptr
        if shape:
            self.shape_estimated = False
            self.shape = shape
        else:
            self.shape_estimated = True
            self.shape = (len(self.indptr) - 1, None)

    def dot(self):
        pass

    def __matmul__(self, x):
        """
        Input: Matrix A stored in CSR, i.e., a list of three lists
                    A = class with attributes data, indices, indptr
               Vector x stored as a list of n (= number of cols) numbers

        Output: Matrix-vector product y = A * x as a list
        """
        y = [0] * (len(self.indptr) - 1)
        for i, pair in enumerate(zip(self.indptr[0:-1], self.indptr[1:])):
            for a_ij, j in zip(
                self.data[pair[0] : pair[1]], self.indices[pair[0] : pair[1]]
            ):
                y[i] += a_ij * x[j]
        return vector(y)

    def toarray(self, col_dim):
        """
        INPUT:
           A: matrix in csr format
        col_dim: its col dimension
        OUTPUT:
        A_dense: list in which each row is densely stored as list
        """
        row_dim = len(self.indptr) - 1
        #  col_dim = self.indptr[0]
        # we store each row of the matrix as a list in the list A_dense
        A_dense = []
        for i in range(row_dim):
            A_dense += [[0] * col_dim]
            nonzero_values = self.data[self.indptr[i] : self.indptr[i + 1]]
            col_indices = self.indices[self.indptr[i] : self.indptr[i + 1]]
            for j in range(len(col_indices)):
                A_dense[i][col_indices[j]] = nonzero_values[j]
        return str(A_dense).replace("],", "]\n")  # A_dense  #


def norm(x, order=2):
    order = float(order)
    return sum([abs(xi) ** order for xi in x]) ** (1.0 / order)


# LEVEL 2
def matvec(A: csr_matrix, x: vector) -> vector:
    """
    computes the matrix vector product
    INPUT:
        A: (mxn) matrix
        x: n-dim vector like
    OUTPUT:
        A*x: matrix-vector product


    Matrix A stored in CSR, i.e., a list of three lists
                    A = [data, indices, indptr]
               Vector x stored as a list of n (= number of cols) numbers

        Output: Matrix-vector product A * x as a list

    """
    y = [0] * (len(A.indptr) - 1)
    for i, pair in enumerate(zip(A.indptr[0:-1], A.indptr[1:])):
        for a_ij, j in zip(A.data[pair[0] : pair[1]], A.indices[pair[0] : pair[1]]):
            y[i] += a_ij * x[j]
    return vector(y)


def average_vector(x: vector) -> vector:
    """
    Compute the result of the following matrix-vector product
            1./n 1 \cdot 1.T \cdot x
    where x is an n-dim vector and 1 is the n-dim one-vector
    """
    length = len(x)
    average = 1.0 / length * sum(x)
    return [average] * length


# ==============================================================#
def diag_quad_csr(A, col_dim):
    data, indices, indptr = A[0], A[1], A[2]

    row_dim = len(A[2]) - 1
    data_diag = []
    indices_diag = []  # list(range(min(col_dim, row_dim)))
    indptr_diag = [0]  # row_dim*[max(row_dim, col_dim)]
    # indptr_diag[0:min(col_dim, row_dim)] = list(range(min(col_dim, row_dim)))

    pointer_count = 0
    for i in range(row_dim):
        nonzero_values = data[indptr[i] : indptr[i + 1]]
        col_indices = indices[indptr[i] : indptr[i + 1]]
        if i in col_indices:
            data_diag += [nonzero_values[col_indices.index(i)]]
            indices_diag += [i]
            pointer_count += 1

        indptr_diag += [pointer_count]

    return [data_diag, indices_diag, indptr_diag]


def inv_diag_quad_csr(A, col_dim):
    """
    INPUT:
    A: a quadratic (!) matrix in csr format
    col_dim: its col dimension
    OUTPUT:
    D^{-1}: the inverse of the diagonal matrix D in csr format (D = diag(A.diagonal()))
    """

    data, indices, indptr = A[0], A[1], A[2]

    row_dim = len(A[2]) - 1
    data_diag = []
    indices_diag = []
    indptr_diag = [0]

    pointer_count = 0
    for i in range(row_dim):
        nonzero_values = data[indptr[i] : indptr[i + 1]]
        col_indices = indices[indptr[i] : indptr[i + 1]]
        if i in col_indices:
            data_diag += [1.0 / nonzero_values[col_indices.index(i)]]
            indices_diag += [i]
            pointer_count += 1

        indptr_diag += [pointer_count]

    return [data_diag, indices_diag, indptr_diag]


def csc_to_dense(A, row_dim):
    """
    INPUT:
    A: matrix in csc format
    row_dim: its row dimension
    OUTPUT:
    A_dense: list in which each column is densely stored as list
    """

    # data, indices, indptr = A[0], A[1], A[2]
    data, indices, indptr = A.data, A.indices, A.indptr

    col_dim = len(indptr) - 1
    # we store each column of the matrix as a list in the list A_dense
    A_dense = []
    for i in range(col_dim):
        A_dense += [[0] * row_dim]
        nonzero_values = data[indptr[i] : indptr[i + 1]]
        row_indices = indices[indptr[i] : indptr[i + 1]]
        for j in range(len(row_indices)):
            A_dense[i][row_indices[j]] = nonzero_values[j]
    return A_dense


def indices_of_occurences(liste, element):
    """get all indices where element appears in liste"""
    result = []
    if element in liste:
        num_of_occ = liste.count(element)
        index_alt = 0
        for i in range(num_of_occ):
            index_neu = index_alt + liste[index_alt:].index(element)
            result += [index_neu]
            index_alt = index_neu + 1
        return result
    else:
        return result


def csc_to_csr(A_csc, dim):
    row_dim, col_dim = dim
    data_csc, indices_csc, indptr_csc = list(A_csc[0]), list(A_csc[1]), list(A_csc[2])

    data_csr = []
    indices_csr = []
    indptr_csr = [0]

    for i in range(row_dim):
        aux = indices_of_occurences(indices_csc, i)

        # build indptr_csr
        indptr_csr += [indptr_csr[i] + len(aux)]

        # build data_csr: for each row index find its occurence in indices and extract respective data_csc
        for j in aux:
            data_csr += [data_csc[j]]

            # build indices_csr: find out their column index
            for k in range(col_dim):
                if indptr_csc[k] <= j < indptr_csc[k + 1]:
                    # print(i, j,k, indptr_csc[k])
                    indices_csr += [k]

    return [data_csr, indices_csr, indptr_csr]


def matmat(A, B):
    col_dim_A = 4  # = row_dim_B  = n
    col_dim_B = 4  # = col_dim_C = ell
    row_dim_A = 4  # = row_dim_C = m

    data_B, indices_B, indptr_B = B[0], B[1], B[2]

    A_csr = csc_to_csr(A, (4, 4))

    data_C = []
    indices_C = []
    indptr_C = [0]

    for i in range(col_dim_B):
        col_i_B = [0] * col_dim_A
        nonzero_values = data_B[indptr_B[i] : indptr_B[i + 1]]
        row_indices = indices_B[indptr_B[i] : indptr_B[i + 1]]
        for j in range(len(row_indices)):
            col_i_B[row_indices[j]] = nonzero_values[j]
        # print(col_i_B)

        col_i_C = matvec(A_csr, col_i_B)

        # print(col_i_C)
        # print()
        count = 0
        for j in range(col_dim_A):
            if col_i_C[j] != 0:
                data_C += [col_i_C[j]]
                indices_C += [j]
                count += 1

        indptr_C += [indptr_C[-1] + count]

    return [data_C, indices_C, indptr_C]
