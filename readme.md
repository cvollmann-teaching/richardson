# Python Project: Richardson Iteration from Scratch and the PageRank

(Under Construction)

- In this project we will implement the [Richardson iteraton](https://en.wikipedia.org/wiki/Modified_Richardson_iteration) from scratch -- an iterative solver for linear systems.

- We will implement our own classes for vectors and CSR matrices (later you can easily substitute them with the corresponding numpy.ndarray and scipy.sparse.csr_matrix).

- We finally apply the code to compute the PageRank (note: with step size 1 the Richardson iteraton is equal to the power iteration with l1-normalization and a discrete probability distribution as initial guess).

## Project Instructions

1. **Initialize a git repository**
   1. github
   2. .gitignore
2. **Plan modularity and setup directory structure**
3. **Working environment: IDE PyCharm**
   1. If applicable: Get educational account with jetbrains
   2. Install PyCharm (professional edition)
   3. Set up virtual environment
   4. Sync requirements.txt
4. **Implementation and Tests**
   1. **Implement class `vector`**
      1. inherit from `list`
      2. overload the operators +, @, * by defining the methods
         1. `__add__`
         2. `__matmul__`
         3. `__mul__`
         4. `__rmul__`
      3. write tests
   2. **Implement class `csr_matrix?`**
      1. initialize with csr tuple `(data, indices,indptr)` and `shape`
      2. implement magic methods
         1. `__matmul__`
         2. `__toarray__`
      3. write tests
   3. **Implement helper function `csrTridiagToep(n, data)` to instantiate tridiag toeplitz matrix in csr format**
   4. **Implement Richardson iteration**
      1. interface: `richardson(A : csr_matrix, b : list, x0 : list, theta=.1, maxiter=500, tol=1e-08)`
   5. **Run examples**
      1. heat equation
      2. tests
   6. **Utils for PageRank**
      1. read from file a network structure as adjacency graph
         1. write tests
      2. compute google matrix
         1. write tests
   7. **Pagerank**
      1. Implement interface to the data (you can use the Scipy Stack here)
      2. Apply Richardson Iteration
5. **Code Documentation with sphinx**
   1. Use at least
      - `.. toctree::`
      - `.. autosummary::`
      - `.. code-block::`
      - `.. autofunction::`
      - `.. autoclass::`
      - `.. math::`
   2. github pages
6. **Software Packaging**
   1. ...
7. **Write Paper with LaTex**
   1. ...
8. **Now run your examples with Scipy Stack**
   1. ...
