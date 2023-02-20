# Python Project: Richardson Iteration from Scratch applied to Heat Equation and the PageRank

(Under Construction)


- This repo contains: the small tutorials (just notes for inclass development, in german), the corresponding instructions (below) and the almost complete worked examples.
  
- In this project we will implement the [Richardson iteraton](https://en.wikipedia.org/wiki/Modified_Richardson_iteration) from scratch -- an iterative solver for linear systems: 

  $$
  x^{k+1} = x^k - \theta\cdot(Ax^k - b),~~~~\theta > 0~\text{small}
  $$

- We will implement our own classes for vectors and CSR matrices and overload common operators such as `+/-, *, @` (later you can easily substitute them with the corresponding numpy.ndarray and scipy.sparse.csr_matrix).

- Heat equation: explicit Euler 

<img src="examples/out/static/heat_equation.gif" alt="heat_equation" style="zoom:60%;" />




- We finally apply the code to compute the PageRank (note: for column stochastic matrices and with step size 1 the Richardson iteraton is equal to the power iteration with l1-normalization and a discrete probability distribution as initial guess).

<img src="examples/out/static/pagerank_small.gif" alt="pagerank_small" style="zoom:80%;" />



## Syllabus

| Time      |       |       | Content                                      | Instructions                        |
| :-------- | ----- | ----- | -------------------------------------------- | ----------------------------------- |
| **Day 1** |       |       |                                              |                                     |
| Session 1 | 10:00 | 11:00 | Mathematical Background I                    |                                     |
| Session 2 |       |       | git, ssh (keys), github                      | [git](#initialize-a-git-repository) |
| Session 3 |       |       | Project Planing and Initialization           |                                     |
| **Day 2** |       |       |                                              |                                     |
| Session 1 | 10:00 | 11:00 | Working Environment                          |                                     |
| Session 2 |       |       | Clean Code                                   |                                     |
| Session 3 |       |       | Software Tests                               |                                     |
| Session 4 |       |       | Implementation: `linalg`                     |                                     |
| **Day 3** |       |       |                                              |                                     |
| Session 1 | 10:00 | 11:00 | Implementation: `linalg`, `iterative_solver` |                                     |
| Session 2 |       |       | Implementation: `example` (Heat Equation 1d) |                                     |
| Session 3 |       |       | Code Documentation with Sphinx               |                                     |
| **Day 4** |       |       |                                              |                                     |
| Session 1 | 10:00 | 11:00 | Mathematical Background II: PageRank         |                                     |
| Session 2 |       |       | Implementation: Pagerank utils and Examples  |                                     |
| Session 3 |       |       | Misc: License, readme, docs,...              |                                     |
| **Day 5** |       |       |                                              |                                     |
| Session 1 | 10:00 | 11:00 | Numpy                                        |                                     |
| Session 2 |       |       | Scipy                                        |                                     |
| Session 3 |       |       | Matplotlib                                   |                                     |












{:toc}


## General Project Instructions

-   Strukturieren Sie Ihre Implementierung sinnvoll. Orientieren Sie sich dabei an der während des Kurses entwickelten Modularisierung.
-   Testen Sie jede einzelne Funktion ausführlich.
-   Verwenden Sie für sämtliche Vektor-- und Matrix--Rechenoperationen nur die von Ihnen implementierten Python--Funktionen (und keine externen Pakete wie z.B. Numpy).
-   Numpy und Scipy können verwendet werden, um die Implementierung zu überprüfen.
-   Bonus\*: Versuchen Sie mögliche Fehleingaben des Nutzers zu antizipieren und mit geeigneten Fehlermeldungen abzupuffern. (Zum Beispiel könnten Dimensionen von $A$ und $b$ nicht zusammenpassen, ein Nutzer könnte die Matrix im falschem Format übergeben, sodass das übergebene Objekt nicht die drei Attribute 'data', 'indices','indptr' aufweist, etc.)

## Initialize a git repository

1. get account on github, set up ssh keys
2. create repo
3. local machine: git clone
4. .gitignore

## Plan modularity and setup directory structure

```bash
|-- code
    |-- data
    |-- docs
    |-- src
    |   |-- linalg.py
    |   |-- iterative_methods.py
    |   |-- utils.py
    |-- examples
    |   |-- confEx1.py
    |   |-- confEx2.py
    |   |-- confTest.py
    |-- tests
    |   |-- test_csr.py
    |-- output
    |-- main.py
    |-- README.md
    |-- LICENSE
    |-- requirements.txt
    |-- .git
    |-- .idea
```



## Working Environment: The IDE PyCharm

1. Get **educational account** with JetBrains: https://www.jetbrains.com/shop/eform/students
2. **Install PyCharm** (Professional edition): https://www.jetbrains.com/help/pycharm/installation-guide.html
3. Set up a **PyCharm Project**: https://www.jetbrains.com/help/pycharm/setting-up-your-project.html
   - Open the directory `code`using the application PyCharm or to play around create any other project.

4. Set up **virtual environment**: https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html
   - Optional: You may want to inherit site-packages from local Python installation
   - Install some packages
   - Add it to `.gitignore`
5. **Run Code**: https://www.jetbrains.com/help/pycharm/running-without-any-previous-configuring.html
   - Familiarize with Python and run some code.
   - Create a Run Configuration
6. Use the **Debugger**: https://www.jetbrains.com/help/pycharm/debugging-code.html
7. Sync **`requirements.txt`**: https://www.jetbrains.com/help/pycharm/managing-dependencies.html
   - Tools| Sync Python requirements
   - Import some package and update the `requirements.txt`. Did it work?
8. **git in PyCharm**
9. Check out the hidden project directory `.idea`
   - Add it to `.gitignore`

10. Further reading:

   - seek and destroy: https://www.jetbrains.com/help/pycharm/auto-completing-code.html

   - refactor https://www.jetbrains.com/help/pycharm/refactoring-source-code.html

   - Code Completion https://www.jetbrains.com/help/pycharm/auto-completing-code.html

   - Konsole https://www.jetbrains.com/help/pycharm/working-with-consoles.html

   - Local History https://www.jetbrains.com/help/pycharm/local-history.html

   - Compare Files https://www.jetbrains.com/help/pycharm/comparing-files-and-folders.html

   - Code Inspection https://www.jetbrains.com/help/pycharm/code-inspection.html



## Clean Code

- Read PEP8 Style Guide: https://www.python.org/dev/peps/pep-0008/
- Good names; 
- Python formatter: `black`
- Code inspection in PyCharm: https://www.jetbrains.com/help/pycharm/tutorial-code-quality-assistance-tips-and-tricks.html#ddc30fc6
- Verwenden Sie bei allen Funktionen und Objekten aussagekräftige Namen und  Docstrings in einem einheitlichen Format (NumPy, Google, reStructuredText).
- consistent docstring (important later for documentation generation). Kommentieren Sie Ihren Code, sodass er für andere gut lesbar ist.




## Implement class `vector` 

In `src/linalg.py`:

1. Inherit from `list` 

   ```python
   class vector(list)
   ```

   We use mutable data type `list()`over `tuple()`as we will later manipulate entries in the vector.

2. Overload the operators `+, -, @` and `*` by implementing the following magic methods which all expect another vector- or scalar-type say `other`:
   - `__add__(self, other)` ($x+y$)
   - `__sub__(self, other)` ($x-y$)
   - `__matmul__(self, other)` ($x^Ty$)
   - `__mul__(self, other)` ($\alpha \cdot x$)
   - `__rmul__(self, other)` ($x\cdot\alpha $)
   - Side remark: Also See Level 1 BLAS Routines:
     - https://de.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms
     - http://www.netlib.org/blas
   
3. Write appropriate test files `test_*.py` which you put into the directory `tests`

   - Create Run Configuration for your tests


## Euclidean Norm

In `src/linalg.py`:

1. Implement a function `norm(x, order=2)` which expects a vector `x` and computes its $p$-Norm:

$$
\mathbb{R}^n \to [0,+\infty),~x \mapsto \|x\|_2 := \left({\sum_{i=1}^n |x_i|^p}\right)^{\frac{1}{p}}
$$

## Implement class `csr_matrix`

In `src/linalg.py`:

1. initialize with CSR-Format (Compressed Sparse Row) tuple `(data, indices,indptr)` and `shape`. Implement at least the following attributes: attributes: `data, indices, indptr, shape`. You can use the following code snippet.

   ```python
   class csr_matrix:
       """
       CSR matrix class
       ...
       """
       def __init__(self, csr_tuple, shape=None):
           _data, _indices, _indptr = csr_tuple
           self.data = _data
           self.indices = _indices
           self.indptr = _indptr
   ```

2. implement magic methods
   1. `__matmul__(self, x : vector) -> vector`
     - This magic method expects a vector `x` and computes the matrix--vector product $A\cdot x$. By operator overloading, for an object `A`  of the class `csr_matrix` we then have:
     - `A @ x = A.__matmul__(x)`                   
     - For simplicity we neglect the capability of evaluating also the matrix--matrix product.
     - Side remark: This next level of complexity can be classified into Level 2 BLAS routines:
          - https://de.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms
          - http://www.netlib.org/blas
   2. `__toarray__(self, col_dim)`
      - A method which outputs a list with the rows of the matrix (again as a list).

3. Write appropriate test files `test_*.py` which you put into the directory `tests`

   - Create Run Configuration for your tests

## Implement helper function `csr_tridiag_toep(n, data)` 

In `src/linalg.py`:

In order to run some examples later on, it would be nice to have a function which creates certain CSR-tuples. For matrices with some particular structure the CSR-lists can be easily obtained. In fact, we implement a function which builds [tridiagonal Toeplitz matrices](https://de.wikipedia.org/wiki/Tridiagonal-Toeplitz-Matrix).

1. Implement a function 

  ```python
  csr_tridiag_toep(n : int, data : tuple) -> csr_matrix
  ```

  that automatically instantiates an object `A`of the above class `csr\_matrix` for a tridiagonal matrix whose diagonals are constant:

```math
  \begin{pmatrix}                              
  b & c  &0   & \cdots   & 0 \\                                               
  a &  b & c  &    &   \vdots \\                                               
  0&  \ddots &  \ddots &\ddots  &0  \\ 
  \vdots  &    &  a &  b & c  \\ 
  0 &   \cdots  & 0& a  &  b \\
  \end{pmatrix}\in \mathbb{R}^{n \times n}.
```

  - Accordingly, the parameter `n` specifies the dimension of the square matrix and the parameter `data` contains the corresponding diagonal entries in the form of a tuple `data = (a,b,c)`.

  - First consider how the three CSR- lists `data, indices, indptr` look like for general parameters `(n, data)` and then implement them as a function depending on `(n, data)`. For instantiation, you then just need to pass these three lists to the constructor of the above class `csr\_matrix`.

2. Write appropriate test files `test_*.py` which you put into the directory `tests`

   - Create Run Configuration for your tests


## Implement Richardson iteration

In `src/iterative_solver.py`:

1. Implement the relaxed Richardson iteration 

   $$
   x_{k+1} = x_k - \theta (Ax_k -b)
   $$
   
   as a function

   ```python
   x, error, numiter = richardson(A : csr_matrix, b : vector, x0 : vector, theta=.1, maxiter=500, tol=1e-08) --> (vector, list, int)
   ```

   which expects as input

   -   `A` : invertible matrix in $\mathbb{R}^{n\times n}$ as object of class **`csr_matrix`**

   -   `b` : rhs in $\mathbb{R}^n$ as object of class `vector` of size $n$

   -   `x0` : initial guess in $\mathbb{R}^n$ as object of class `vector` of size $n$

   -   `theta` : relax. parameter/stepsize $\theta$ as `float`

   -   `maxiter` : maximal number of iterations as `int`

   -   `tol` : error tolerance as `float`

   and outputs

   -   `x` : the last iterate (approxiamte solution) as object of class `vector` of size $n$

   -   `error` : Python list of all residuals $\|Ax_k-b\|_2$

   -   `numiter` : number of iterations that have  been performed

   The procedure should terminate as soon as the residual is sufficiently small, i.e. $\|Ax_k-b\|_2 < \texttt{tol}$ or the maximum number `maxiter` of iteration steps is reached.

2. Write appropriate test files `test_*.py` which you put into the directory `tests`

   - Create Run Configuration for your tests

See also LAPACK built on BLAS: https://de.wikipedia.org/wiki/LAPACK





## Run first examples: 1d Heat Equation

1. **Heat Equation**

   Solve $A_1x =b$, with
   
```math
A_1 = n^2 \begin{pmatrix}                                
2 & -1  &0   & \cdots   & 0 \\                                               
-1 &  2 & -1  &    &   \vdots \\                                               
0&  \ddots &  \ddots &\ddots  &0  \\ 
\vdots  &    &  -1 &  2 & -1  \\ 
0 &   \cdots  & 0& -1  &  2 \\
\end{pmatrix}\in \mathbb{R}^{n \times n},
~~~b = \begin{pmatrix}                                
1 \\                                               
\\                                               
\vdots  \\ 
\\ 
1  \\ 
\end{pmatrix} \in \mathbb{R}^{n}, 
~~~x_0 =  \begin{pmatrix}                             
0 \\                                               
\\                                               
\vdots  \\ 
\\ 
0  \\ 
\end{pmatrix}\in \mathbb{R}^{n},
```

   for different dimensions $n$ (should be a parameter in your config script).

2. **Regularized Heat Equation**

   Replace $A_1$ in the above example with
   
$$
   A_2 = A_1 + \delta I
$$

for $\delta > 0$ and $I \in \mathbb{R}^{n\times n}$ the identity matrix. Run your examples from 1. again with different $\delta$.   Observe the number of iterations needed as $\delta$ increases. What about the convergence now?


**Remarks:**

-   Put the configuration for these examples in `examples/example1.py` etc. and run your examples in `main.py` where you mainly call the function `richardson`with the input parameters defined in the example files.
    
-   If your method does not converge, try it with a (very) small relaxation parameter $\theta$ and a large
    maximum number of iterations `maxiter`. The matrix $A_1$ above is "ill-conditioned" and the Richardson method may need (very!) many iterations to achieve a sufficiently small error. For matrix $A_2$, on the other hand, you should observe a significant improvement for increasing $\delta$.
    
-   The matrices $A_1$ and $A_2$ are respectively tridiagonal--Toeplitz- matrices. So you can use your `csrTridiagToep` function from above to instantiate the `csr_matrix` class.
    
-   You will recognize the matrix $A_1$ later as a finite-difference discretization of the one-dimensional Poisson equation on regular grids with homogeneous Dirichlet boundary values. And the matrix $A_2$ as a Tikhonov-regularization of it.

## Utils

In `src/utils.py`:

Implement:

1. A function to plot a univariate function (in our case the vector of residuals `error`) using `matplotlib.pyplot`.

   Erstellen Sie mindestens einen Plot. Zum Beispiel könnten Sie die Funktion
   k 7→ kAx k − bk 2 (= error[k]),
   also den Fehler-Verlauf, zeichnen. Speichern Sie die Grafik mit einem aussagekräftigen Namen als .pdf-Datei
   im Ordner ‘code/output/’, um sie in Ihr L A TEX-Dokument zu importieren.
   → Dafür benötigen Sie die Liste error und das Modul matplotlib.pyplot (savefig()).

2. Optional: A function that uses the Python package `tabulate`to generate a LaTex table into an external text file with two columns being iteration number and corresponding entry in the residual vector `error` that you can import later on into your paper. (Optional third column would be the rate of convergence)

## Utils for PageRank

- Recommended Reading: [Deeper Inside PageRank](https://www.stat.uchicago.edu/~lekheng/meetings/mathofranking/ref/langville.pdf) by Langville and Meyer.

- create a script `src.pagerank_utils` (or similar)

  

1. Read edgle list into scipy sparse csr

2. Normalize rows

3. Deal with dangling nodes (pdf pages or similar)

4. Implement google_matrix as class with correct matmul

5. For richardson: Implement a second version with the following adatption

6. combine everything

7. Write appropriate test files `test_*.py` which you put into the directory `tests`

   - Create Run Configuration for your tests

8. Optional: Write further utils to draw the graphs, create a video, ...

   

## Compute the Pagerank

1. **PageRank of your own Graph**
   1. Draw your own small and write the corresponding list of edges textfile: `examples/pagerank_small.edges`
   2. Create an example config like `example/pagerank_small`
   3. 

2. **Download real data:** https://networkrepository.com/web.php

## Implement the Power Iteration (optional)

1. Implement a function `power_iteration(A,...)`
2. Re-run your Page-Rank using the power iteration and the Google matrix.



## Code Documentation with Sphinx

1.  Consult the official documentation: https://www.sphinx-doc.org/en/master/index.html

2.  Generate an html documentation of your code using `sphinx`. Implement at least the following points:

    -   Deliberately choose an `html_theme`

    -   At a minimum, use the following directives:

        -   `.. toctree::`

        -   `.. autosummary::`

        -   `.. code-block::`

        -   `.. autofunction::`

        -   `.. autoclass::`

        -   `.. math::`

    -   Use the extension `sphinx.ext.viewcode`

    -   Create at least one more subpage and link to it.
        
    -   Use consistent docstrings in a fixed format.
3.  Use github pages to expose your documentation.
4.  Link your documentation later on in your paper.

## Software Packaging (optional)

create a python package.

## Write a Paper with LaTeX (optional)

Read the Overleaf Tutorials by starting here: https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes

9.4
Setzen von Text
https://dante-ev.github.io/l2kurz/l2kurz.pdf#section.3
9.5
Setzen von mathematischen Formeln
https://dante-ev.github.io/l2kurz/l2kurz.pdf#section.4
9.6
Setzen von Bildern
https://dante-ev.github.io/l2kurz/l2kurz.pdf#section.5
9.7
Seitenaufbau
https://dante-ev.github.io/l2kurz/l2kurz.pdf#section.6



### Warmup: LaTeX via Command Line

 \
(evlt. inclass vorführen mit GUI und Terminal nebeneinander)

1. VPN Verbindung herstellen

2. ssh auf remote (syrma.uni-trier.de) \[ggf. über web-interface
   guacamole\]

3. im home-Verzeichnis:\
   Ein .tex-Skript mit einem Editor, zB nano, anlegen 

   \$ nano text.tex

   und ein paar LaTeX-Befehle wie einbauen; Minimalbeispiel\
   \
   \
   \
   \...\
   \

4. LaTeX-Compiler, hier `pdflatex`, auf diese Datei anwenden

   \$ pdflatex text.tex

5. Datei im Terminal anschauen z.B. via

   \$ less text.pdf

   oder, falls X-Window vorhanden, mit einem pdf-Betrachter anschauen, zB:

   \$ xdg-open text.pdf

6. .pdf Datei auf die lokale Maschine kopieren, zB via sftp

   \$ sftp vollmann@syrma.uni-trier.de

   oder im Dateimanager:

   sftp://vollmann@syrma.uni-trier.de

### Working Environment: The IWE TexStudio 

1.  Laden Sie  herunter und installiere es auf Deinem System: <https://www.texstudio.org/#Download>

2.  Führen Sie die Schritte von oben nun mit  TexStudio anstatt über die Konsole aus.

### Plan Modularity 

```bash
|-- text/
    |-- src/
    |   |-- macros/
    |   |   |-- meta.tex
    |   |   |-- usepackages.tex
    |   |   |-- style.tex
    |   |   |-- commands.tex
    |   |   |-- ...
    |   |-- content/
    |   |   |-- abstract.tex
    |   |   |-- introduction.tex
    |   |   |-- section1.tex
    |   |   |-- section2.tex
    |   |   |-- listing.py
    |   |   |-- ...    
    |-- media/
    |   |-- picture.png
    |   |-- picture.jpg
    |   |-- ...
    |-- literature/
    |   |-- literature.bib
    |   |-- pdfs/
    |   |   |-- book.pdf      
    |   |   |-- paper.pdf   
    |   |   |-- ... 
    |-- main.tex
```





Legen Sie die folgenden Verzeichnisse und Dateien von Abbildung
[\[fig:vz-struktur-text\]](#fig:vz-struktur-text){reference-type="ref"
reference="fig:vz-struktur-text"} an:

1.  `<PATH>/meta.tex`

    -   Mindestens folgende Variablen setzen:\
        `\title{<ProjektName>}`\
        `\author{Name}` mit\
        `\date{Jahr (, Datum, today)}`

2.  `<PATH>/usepackages.tex`

    -   hier können alle benötigten Pakete geladen werden

    -   

3.  `<PATH>/style.tex`

    -   Hier kann alles konfiguriert werden, was das Erscheinigungsbild
        des Textes beeinflusst.

    -   Beispiele: Farben, Theorem-Umgebungen, Links,\...

4.  `<PATH>/commands.tex`

    -   Hier können alle definierten Konstrukte zentral gesammelt
        werden\
        , , , \...

5.  `<PATH>/literature.bib`

    -   In dieser Datenbank wird die Literatur gesammelt.

    -   Setzen Sie hier mindestens einen Eintrag, der dann im Text
        zitiert wird.

    -   In dem Verzeichnis `<PATH>/literature/` können beispielsweise
        auch die pdf Dateien dazu aufbewahrt werden

6.  `<PATH>/abstract.tex`

    -   Schreiben Sie eine kleine Zusammenfassung Ihres Aufsatzes. \...

7.  `<PATH>/<InhaltsBaustein>.tex`

    -   Hier verfassen wir den eigentlichen Inhalt.

    -   Der Inhalt kann wiederum auf mehrere Bausteine verteilt werden.

    -   In dieser Datei: ``

    -   mindestens einen bib Eintrag zitieren

8.  `<PATH>/main.tex`\
    Haupteingabedatei mithilfe derer wir alles zusammenkleben. Siehe
    Abbildung [\[fig:main.tex\]](#fig:main.tex){reference-type="ref"
    reference="fig:main.tex"} für einen möglichen Aufbau.\
    Die **Mindestanforderungen** an das Projekt sind:

    -   importiere .tex-Bausteine via (oder , ,\...)

    -   Titelseite mit Abstract

    -   Table of Content

    -   List of Figures mit mindestens einem Eintrag (erstellen Sie
        mindestens eine Grafik)

    -   List of Tables mit mindestens einem Eintrag (erstellen Sie
        mindestens eine Tabelle)

    -   \|

    -   Inhalt\
        \>\> Setzen Sie einen Link auf Ihre HTML-Dokumentation (z.B.
        mithilfe eines geeigneten BibTex--Eintrags)

    -   \|

    -   Literaturverzeichnis mit mindestens einem Eintrag (zitieren Sie
        mindestens ein Lehrbuch, das zum Projekt passt)

**Bemerkung:** Projekt-spezifisch sind im Wesentlichen die Dateien
`meta.tex, abtract.tex, <InhaltsBaustein>.tex, literature.bib`. Sofern
der Kontext ähnlich ist, müssen wir für ein neues Projekt nur diese
Dateien austauschen!

**Mathematischer Aufsatz**
Verfassen Sie einen kurzen mathematischen Aufsatz 

$$\texttt{<PATH>/text/}$$ 

mit LaTeX über das Richardson--Verfahren und stellen Sie Ihre numerischen Ergebnisse vor. Modularisieren Sie Ihr LaTeX--Projekt sinnvoll und setzen Sie die oben erwähnten **Mindestanforderungen** um.

## Run your examples with Scipy Stack (optional)
