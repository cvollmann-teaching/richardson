# ---------------#
#  numerical LA
# ---------------#
from src.linalg import *


def richardson(
        A: csr_matrix,
        b: vector,
        x: vector,
        theta=0.1,
        maxiter=50,
        tol=1e-06,
        callback=None,
        **kwargs
):
    """
    solves a system Ax = b, where A is assumed to be invertible,
    with relaxed splitting methods: Jacobi, Richardson

    Parameters
    ----------
    A : (n, n) matrix as csr class with the 3 csr attributes
         system matrix
    b : list of length n (or numpy.ndarray)
         right-hand side
    x: list of length n (or numpy.ndarray)
         initial guess
    theta : number (int or float)
            relaxation parameter (step length) default theta = 0.1
    tol : number (float)
            error tolerance, iteration stops if ||Ax-b|| < tol
    maxiter : int
        number of iterations that are performed , default m=50

    Returns
    -------
    x : list of length m (or less), containing iterates
        columns represent iterates from x_0 to x_(m-1)
    X :
    error :
    numit :
    """
    b = vector(b)
    x = vector(x)
    error = []
    for k in range(maxiter):
        if callback:
            callback(x, **kwargs)
        ek = A @ x - b
        error += [norm(ek)]
        if error[-1] < tol:
            return x, error, k
        x = x - theta * ek
    return x, error, k


def power_iteration(A, m, p=1):
    """
    Solves eigenvalue problem via Power Method
    Expects the largerst eigenvalue of A to be scritly larger

    Parameters
    ----------
    A : (n,n) ndarray
        matrix
    m : int
        number of iterations
    p : int or numpy.inf, optional
        specifying the order of the p-Norm used for normalization

    Returns
    -------
    x : (n,1) ndarray
        normalized (with p-Norm) eigenvector for largest eigenvalue
    mu : float
         the largest eigenvalue
    """
    n = A.shape[1]
    x = [1.0 / n] * n
    for k in range(m):
        z = A @ x
        x = (1.0 / norm(z, order=p)) * z
        mu = (x @ z) / (x @ x)
    return x, mu
