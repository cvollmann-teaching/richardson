import scipy.sparse as sparse
import networkx as nx
import numpy as np
import src.linalg
import matplotlib.pyplot as plt


def read_edgelist_to_csr(filename: str) -> sparse.csr_matrix:
    """
    reads directed graph from textfile in list of edges format
    returns scipy sparse csr matrix
    """
    g = nx.read_edgelist(filename, nodetype=int, create_using=nx.DiGraph)
    g = nx.to_scipy_sparse_array(g)
    g = sparse.csr_matrix(g)
    return g


def draw_graph_from_edgeslist(filename: str):
    g = nx.read_edgelist(filename, nodetype=int, create_using=nx.DiGraph)
    fig, ax = plt.subplots()
    nx.draw_networkx(g, pos=nx.kamada_kawai_layout(g))
    ax.axis("Off")
    ax.set_title("{title}".format(title="Example Graph"))
    plt.show()
    return None


def normalize_rows(g: sparse.csr_matrix) -> sparse.csr_matrix:
    """
    normalizes rows of a scipy sparse csr matrix
    """
    row_sum = g.sum(axis=1)
    # normalize rows
    row_sum[row_sum == 0] = 1
    g = g.multiply(1.0 / row_sum)
    g = g.tocsr()
    return g


def un_dangle(G):
    """
    nodes without outgoing links produce zero rows in adjacency matrix
    we put one on the diagonals of these rows (personalization vector = unit vector)
    """
    row_sum = G.sum(axis=1)
    n = len(row_sum)
    diag = np.zeros((n, 1))
    diag[row_sum == 0] = 1
    G += sparse.diags(diag.flatten())
    return G


class google_matrix:
    """
    expects normalized, undangled and transposed adjacency matrix P
    and damping factor \alpha

    implements matrix-vector product with google matrix
    with uniform stochastic pertubation matrix
    """

    def __init__(self, _P, _alpha=0.75):
        self.P = _P
        self.alpha = _alpha
        self.shape = _P.shape

    def __matmul__(self, x):
        result = self.alpha * (self.P @ x)
        # note that type "vector" does not support broadcasting!
        result += src.linalg.vector([(1 - self.alpha) * sum(x) / len(x)] * len(x))
        return result


class transition_rate_matrix:
    """
    for richardson: (I - P)
    transition rate matrix for Markov chain is acutally the M-matrix: Q:=(P-I)
    Thus in each richardson step we do: x_new = x_old + Q*x_old

    expects normalized, undangled and transposed adjacency matrix P
    and damping factor \alpha

    implements matrix-vector product with google matrix
    with uniform stochastic pertubation matrix
    """

    def __init__(self, _P, _alpha=0.75):
        self.P = _P
        self.alpha = _alpha
        self.shape = _P.shape

    def __matmul__(self, x):
        result = x - self.alpha * (self.P @ x)
        # note that type "vector" does not support broadcasting!
        result = result - src.linalg.vector(
            [(1 - self.alpha) * sum(x) / len(x)] * len(x)
        )
        return result


def read_google_matrix(filename, alpha=0.75):
    G = read_edgelist_to_csr(filename)
    G = normalize_rows(G)
    G = un_dangle(G)
    G = G.transpose()
    P = google_matrix(G, alpha)
    return P


def read_transition_rate_matrix(filename, alpha=0.75):
    G = read_edgelist_to_csr(filename)
    G = normalize_rows(G)
    G = un_dangle(G)
    G = G.transpose()
    P = transition_rate_matrix(G, alpha)
    return P
