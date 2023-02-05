maxiter = 20
theta = 0.3
A_data = [3, -1, -1, 3, -1, -1, 3, -1, -1, 3, -1, -1, 3]
A_indices = [0, 1, 0, 1, 2, 1, 2, 3, 2, 3, 4, 3, 4]
A_indptr = [0, 2, 5, 8, 11, 13]
n = 5
b = n * [1]
x0 = n * [0]

import src.linalg
A = src.linalg.csr_matrix((A_data, A_indices, A_indptr))








