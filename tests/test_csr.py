from src.linalg import csr_matrix


def test_example():
    # Example
    data = [1, 2, 3]
    indices = [0, 1, 2]
    indptr = [0, 1, 2, 3]
    col_dim = 3
    A = csr_matrix((data, indices, indptr))
    print(A.toarray(3))
    #    print(A.data, A.indices, A.indptr)
    x = [1] * col_dim
    print(A @ x)
