import scipy.sparse as scs
from src.linalg import vector

save_path = "examples/out/heat_equation.gif"
n = 50
A = n**2 * (2 * scs.eye(n, k=0) - scs.eye(n, k=-1) - scs.eye(n, k=1))
x0 = vector([0] * n)
b = vector([1] * n)
maxiter = 10000
theta = 0.0001
# A = A + 0.01 * scs.eye(n)

# import scipy.sparse.linalg as linalg
# # print(linalg.eigs(A))
