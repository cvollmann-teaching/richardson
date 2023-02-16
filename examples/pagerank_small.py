import src.linalg
import src.pagerank_utils

filename = "examples/pagerank_small.edges"
alpha = 0.7
A = src.pagerank_utils.read_google_matrix_2(filename, alpha=alpha)
n = A.shape[0]
maxiter = 200
theta = 1.0
b = src.linalg.vector(n * [0])
x0 = src.linalg.vector(n * [0])
x0[1] = 1
