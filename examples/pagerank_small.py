import src.linalg
import src.pagerank_utils

filename = "examples/pagerank_small.edges"
src.pagerank_utils.draw_graph_from_edgeslist(filename)
alpha = 0.7
A = src.pagerank_utils.read_transition_rate_matrix(filename, alpha=alpha)
n = A.shape[0]
maxiter = 200
theta = 1.0  #  important to keep Markov chain modell of the PageRank
b = src.linalg.vector(n * [0])
x0 = src.linalg.vector(n * [0])
x0[1] = 1
