import scipy.sparse as scs
import numpy as np
from src.linalg import vector

# maxiter = 2000
# theta = 0.8
# A = scs.csr_matrix(0.25 * np.array([[2, -1], [-1, 2]]))
# n = 2
# x0 = [4, 1.4]
# b = n * [0]

save_path = "examples/out/heat_equation.gif"
n = 50
A = n**2 * (2 * scs.eye(n, k=0) - scs.eye(n, k=-1) - scs.eye(n, k=1))
# A[0,0] = 1
# A[0,1] = 0
# A[-1, -1] =  1
# A[-1, -2] = 0
# A = float(n**2) * A
# A[0,0] = 1
# A[-1,-1] = 1
x0 = vector([0] * n)
b = vector([1] * n)
maxiter = 10000
theta = 0.0001
# A = A + 0.01 * scs.eye(n)

# import scipy.sparse.linalg as linalg
# import numpy as np
# # print(linalg.eigs(A))
# print(np.max(np.abs(linalg.eigs(np.eye(n)-theta*A)[0])))
