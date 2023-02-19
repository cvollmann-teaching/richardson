import src.linalg
import src.pagerank_utils

filename = "examples/pagerank_small.edges"
save_path = "examples/out/pagerank_small.gif"
src.pagerank_utils.draw_graph_from_edgeslist(filename)
alpha = 0.85
A = src.pagerank_utils.read_transition_rate_matrix(filename, alpha=alpha)
n = A.shape[0]
maxiter = 25
theta = 1.0  #  important to keep Markov chain modell of the PageRank
b = src.linalg.vector(n * [0])  # important for correct fixed point set up
x0 = src.linalg.vector(n * [1.0 / n])
