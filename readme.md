# Python Project: Richardson Iteration from Scratch and the PageRank

(Under Construction)


- In this project we will implement the [Richardson iteraton](https://en.wikipedia.org/wiki/Modified_Richardson_iteration) from scratch -- an iterative solver for linear systems: 
  $$
  x^{k+1} = x^k + \theta p^k=x^k - \theta(Ax^k - b),~~~~\theta > 0~\text{klein}
  $$

- We will implement our own classes for vectors and CSR matrices (later you can easily substitute them with the corresponding numpy.ndarray and scipy.sparse.csr_matrix).

- We finally apply the code to compute the PageRank (note: for column stochastic matrices and with step size 1 the Richardson iteraton is equal to the power iteration with l1-normalization and a discrete probability distribution as initial guess).


{:toc}


## General Project Instructions

-   Strukturieren Sie Ihre Implementierung sinnvoll. Orientieren Sie sich dabei an der während des Kurses entwickelten Modularisierung.
    
-   Testen Sie jede einzelne Funktion ausführlich.

-   Verwenden Sie bei allen Funktionen und Objekten aussagekräftige Namen und  Docstrings in einem einheitlichen Format (NumPy, Google, reStructuredText).
    
-   Kommentieren Sie Ihren Code, sodass er für andere gut lesbar ist.

-   Verwenden Sie für sämtliche Vektor-- und Matrix--Rechenoperationen nur die von Ihnen implementierten Python--Funktionen (und keine externen Pakete wie z.B. Numpy).
    
-   Numpy und Scipy können verwendet werden, um die Implementierung zu überprüfen.
    
-   Bonus\*: Versuchen Sie mögliche Fehleingaben des Nutzers zu antizipieren und mit geeigneten Fehlermeldungen abzupuffern. (Zum Beispiel könnten Dimensionen von $A$ und $b$ nicht zusammenpassen, ein Nutzer könnte die Matrix im falschem Format übergeben, sodass das übergebene Objekt nicht die drei Attribute 'data', 'indices','indptr' aufweist, etc.)

## Initialize a git repository

1. ssh keys
2. github
3. .gitignore

## Plan modularity and setup directory structure

1. src
2. tests
3. examples
4. docs
5. ...

```bash
|-- code
    |-- docs
    |-- src
    |   |-- linalg.py
    |   |-- iterSolver.py
    |   |-- helpers.py
    |-- examples
    |   |-- confEx1.py
    |   |-- confEx2.py
    |   |-- confTest.py
    |-- output
    |-- main.py
    |-- README.rst
    |-- requirements.txt
    |-- .git
    |-- .idea
```



## Working environment: The IDE PyCharm

1. If applicable: Get **educational account** with jetbrains under https://www.jetbrains.com/shop/eform/students
2. **Install PyCharm** (professional edition): https://www.jetbrains.com/help/pycharm/installation-guide.html
3. Set up a **PyCharm Project**: https://www.jetbrains.com/help/pycharm/setting-up-your-project.html
4. Set up **virtual environment**: https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html
   1. In the Settings/Preferences dialog: Ctrl+Alt+S | Project: <project name> | \textbf{Python Interpreter} | 
   2. inherit site-packages: Optional können wir auch Pakete von der lokalen systemweiten Python Installation vererben
   3. Pakete  hinzufügen
5. Run Code: https://www.jetbrains.com/help/pycharm/running-without-any-previous-configuring.html
   1. Run | Edit Configuration
6. Sync requirements.txt: https://www.jetbrains.com/help/pycharm/managing-dependencies.html
   1. \textbf{Tools} | \textbf{Sync Python requirements}
   2. Mal ein anderes Paket installieren \textbf{und} verwenden/importieren.\ Dann \texttt{requirements.txt} updaten. Wurde das Paket hinzugefügt?



## Implement class `vector`

1. inherit from `list` 

   ```python
   class vector(list)
   ```

   Warum list() (anstatt z.B. tuple())? Da wir Vektoren und Matrizen durch numerische Berechnungen und Verfahren manipulieren möchten, liegt es nahe, dass wir einen \textit{veränderlichen} Datentyp wählen.

2. overload the operators +, @, * by defining the magic methods
   - `__add__`
   - `__matmul__`
   - `__mul__`
   - `__rmul__`
   - Also See Level 1 BLAS Routines:
     - https://de.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms
     - http://www.netlib.org/blas

3. Write tests

## Euklidische Norm:   

$\mathbb{R}^n \to [0,+\infty),~x \mapsto \|x\|_2 := \sqrt{\sum_{i=1}^n x_i^2}$

​		$$\texttt{nrm(x : list)}$$

## Implement class `csr_matrix`

1. initialize with CSR-Format (Compressed Sparse Row) tuple `(data, indices,indptr)` and `shape`
2. attributes
   1. data, indices, indptr, shape
3. implement magic methods
   1. `__matmul__(self, x)`
      - Diese magische Methode nimmt einen Vektor \texttt{x} als Liste entgegen und berechnet das Matrix--Vektor Produkt $A\cdot x$. Durch die Operatorüberladung gilt dann für ein Objekt \texttt{A} der hiesigen Klasse die Gleichung
        						$$\texttt{A @ x = A.\_\_matmul\_\_(x)} $$
      - Die magische Funktion \texttt{\_\_matmul\_\_($self$, x)} (und damit der Operator \texttt{@}) kann typischerweise auch das Matrix--Matrix Produkt auswerten. Das vernachlässigen wir hier der Einfachheit halber.
      - Level 2 BLAS Routines:
        - https://de.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms
        - http://www.netlib.org/blas
   2. `__toarray__()`
      - ​	Eine Methode, welche eine Liste mit den Zeilen der Matrix (wiederum als Liste) ausgibt.
4. write tests

## Implement helper function `csrTridiagToep(n, data)` 

to instantiate tridiag toeplitz matrix in csr format

- Implementieren Sie eine Funktion $$\texttt{A = csrTridiagToep(n, data)},$$ die ein Objekt \texttt{A} der obigen Klasse \texttt{csr\_matrix} automatisch erzeugt für eine Tridiagonal-Matrix deren Diagonalen konstant sind:
  $$\left(\begin{array}{rrrrr}                                
  b & c  &0   & \cdots   & 0 \\                                               
  a &  b & c  &    &   \vdots \\                                               
  0&  \ddots &  \ddots &\ddots  &0  \\ 
  \vdots  &    &  a &  b & c  \\ 
  0 &   \cdots  & 0& a  &  b \\
  \end{array}\right)\in \mathbb{R}^{n \times n}.$$
- Demnach gibt der Parameter \texttt{n} (\texttt{int}) die Dimension der quadratischen Matrix an und der Parameter \texttt{data} enthält die entsprechenden Diagonaleinträge (zum Beispiel in Form einer Liste \texttt{[a,b,c]}).
- Überlegen Sie sich zunächst wie die drei CSR--Listen \texttt{data, indices, indptr} hier im Allgemeinen (d.h. für allgemeine Parameter \texttt{n, data}) aussehen und implementieren Sie diese anschließend als Funktion abhängig von \texttt{(n, data)}. Zur Instanzerzeugung müssen Sie diese drei Listen dann nur noch an den Konstruktor der obigen Klasse \texttt{csr\_matrix} übergeben.
- https://de.wikipedia.org/wiki/Tridiagonal-Toeplitz-Matrix

## Implement Richardson iteration

1. interface: `richardson(A : csr_matrix, b : list, x0 : list, theta=.1, maxiter=500, tol=1e-08)`

2. die das relaxierte Richardson-Verfahren
   $$x_{k+1} = x_k - \theta (Ax_k -b)$$ implementiert. Als Eingabe wird
   erwartet:

   -   `A` : invertierbare Matrix aus $\R^{n\times n}$ als Objekt der
       Klasse **`csr_matrix`**

   -   : rechte Seite aus $\Rn$ als Python-Liste der Länge $n$

   -   : Startvektor aus $\Rn$ als Python-Liste der Länge $n$

   -   : Relaxationsparameter $\theta$ als float

   -   : maximale Iterationszahl als int

   -   : Fehlertoleranz als float

   und folgende Ausgabe tätigt

   -   : die aktuelle Iterierte (approximierte Lösung) als Python-Liste der
       Länge $n$

   -   : Python-Liste mit allen Residuen $\|Ax_k-b\|_2$

   -   : Anzahl an Iterationen, die durchgeführt wurden, als int

3. Das Verfahren soll abbrechen, sobald das Residuum hinreichend klein ist, d.h.
   $$\|Ax_k-b\|_2 < \ttt{tol}$$
   oder die maximale Anzahl \ttt{maxiter} an Iterationsschritten erreicht ist. 

4. see LAPACK built on BLAS: https://de.wikipedia.org/wiki/LAPAC

## Run examples

1. heat equation

    Lösen Sie	
   $$
   A_1 = n^2 \left(\begin{array}{rrrrr}                                
   		2 & -1  &0   & \cdots   & 0 \\                                               
   		-1 &  2 & -1  &    &   \vdots \\                                               
   		0&  \ddots &  \ddots &\ddots  &0  \\ 
   		\vdots  &    &  -1 &  2 & -1  \\ 
   		0 &   \cdots  & 0& -1  &  2 \\
   		\end{array}\right)\in \mathbb{R}^{n \times n}, 
   		~~~~b = \left(\begin{array}{rrrrr}                                
   		1 \\                                               
   		\\                                               
   		\vdots  \\ 
   		\\ 
   		1  \\ 
   		\end{array}\right) \in \mathbb{R}^{n}, 
   		~~~x_0 =  \left(\begin{array}{rrrrr}                                
   		0 \\                                               
   		\\                                               
   		\vdots  \\ 
   		\\ 
   		0  \\ 
   		\end{array}\right) \in \mathbb{R}^{n},
   $$
   für \underline{verschiedene} Dimensionen $n$.

2. regularized heat equation

   Ersetzen Sie $A_1$ im obigen Beispiel durch
   		$$
   		A_2 = A_1 + \delta I$$
   		für $\delta > 0$ und $I \in \Rnn$ die Identitätsmatrix. Lassen Sie Ihre Beispiele von 1. nochmal laufen mit verschiedenen $\delta$.   Beobachten Sie dabei die Anzahl benötigter Iterationen bei steigendem $\delta$. Wie sieht es nun mit der Konvergenz aus?

3. tests

-   Falls Ihr Verfahren nicht konvergiert, versuchen Sie es mit einem
    (sehr) kleinen Relaxationsparameter $\theta$ und einer großen
    maximalen Iterationsanzahl `maxiter`. Die obige Matrix $A_1$ ist
    "schlecht konditioniert" und das Richardson--Verfahren kann (sehr!)
    viele Iterationsschritte benötigen, um einen hinreichend kleinen
    Fehler zu erzielen. Bei der Matrix $A_2$ sollten Sie hingegen für
    steigende $\delta$ eine deutliche Verbesserung beobachten.

-   Die Matrizen $A_1$ und $A_2$ sind jeweils
    Tridiagonal--Toeplitz--Matrizen. Sie können also Ihre Funktion
    `csrTridiagToep` von oben zur Instanziierung der Klasse `csr_matrix`
    verwenden.

-   Die Matrix $A_1$ werden Sie später als Finite--Differenzen
    Diskretisierung der eindimensionalen Poisson-Gleichung auf regulären
    Gittern mit homogenen Dirichlet--Randwerten wiedererkennen. Und die
    Matrix $A_2$ als Tikhonov--Regularisierung davon.

## Utils for PageRank

1. read from file a network structure as adjacency graph
   1. write tests
2. compute google matrix
   1. write tests

## Pagerank

1. Implement interface to the data (you can use the Scipy Stack here)
2. Apply Richardson Iteration



## Code Documentation

1.  Lesen Sie die offizielle Dokumentation:

    <https://www.sphinx-doc.org/en/master/index.html>

2.  Generieren Sie eine html--Dokumentation Ihres Codes mithilfe von `sphinx`. Setzen Sie dabei mindestens die folgenden Punkte um:

    -   Wählen Sie bewusst ein `html_theme`

    -   Verwenden Sie mindestens die folgenden Direktiven:

        -   `.. toctree::`

        -   `.. autosummary::`

        -   `.. code-block::`

        -   `.. autofunction::`

        -   `.. autoclass::`

        -   `.. math::`

    -   Verwenden Sie die extension `sphinx.ext.viewcode`

    -   Legen Sie mindestens eine weitere Unterseite an und verlinken Sie diese.
        
    -   Verwenden Sie konsistente docstrings in einem festen Format.

3.  Setzen Sie später in Ihrem Aufsatz einen Link auf die entsprechende html--Datei. Links auf eine lokale `html` Dateien können sie wie folgt
    in LaTex setzen: $$\latexCommand{url}{file://<ABSOLUTER-DATEIPFAD>}$$

4.  Use at least

    - `.. toctree::`

    - `.. autosummary::`

    - `.. code-block::`

    - `.. autofunction::`

    - `.. autoclass::`

    - `.. math::`

5.  Use github pages to expose your documentation.

## Software Packaging

1. ...

## Write Paper with LaTeX

**LaTeX über die Konsole**\
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

** TexStudio installieren und nutzen**\

1.  Laden Sie  herunter und installiere es auf Deinem System: <https://www.texstudio.org/#Download>

2.  Führen Sie die Schritte von oben nun mit  anstatt über die Konsole
    aus.

**Text--Projekt modularisieren**

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

## Run your examples with Scipy Stack

1. ...
