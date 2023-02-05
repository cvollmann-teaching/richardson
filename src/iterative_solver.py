# ---------------#
#  numerical LA
# ---------------#
from src.linalg import *


def richardson(A : csr_matrix, b :vector, x : vector, theta=.1, maxiter=50, tol=1e-06):
    """
    solves a system Ax = b, where A is assumed to be invertible,
    with relaxed splitting methods: Jacobi, Richardson

    Parameters
    ----------
    A : (n, n) matrix as csr class with the 3 csr attributes
         system matrix
    b : list of length n (or numpy.ndarray)
         right-hand side
    x0: list of length n (or numpy.ndarray)
         initial guess
    method : string
             indicates method: "Richardson" (=default)
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
    # error = []
    # for k in range(maxiter):
    #     ek = vec_diff(matvec(A, x), b)
    #     error += [norm(ek)]
    #     if error[-1] < tol:
    #         return x, error, k
    #     pk = vec_scaling(ek,theta)
    #     x = vec_diff(x, pk)
    # return x, error, k

    error = []
    for k in range(maxiter):
        ek = A @ x - b
        error += [norm(ek)]
        if error[-1] < tol:
            return x, error, k
        x = x - (theta * ek)
    return x, error, k
