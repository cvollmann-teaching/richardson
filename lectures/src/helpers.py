def plot2d_iterates(X, path="output/2diterates.pdf", dpi=400):
    import matplotlib.pyplot as plt

    plt.figure()
    for i in range(len(X)):
        plt.plot(X[i][0], X[i][1], "ro--")
    # plt.legend(methods)
    plt.title("Iterates x_k")
    plt.axis("equal")
    plt.savefig(path, dpi=dpi)
    return


def plot1d(X, path="output/1d.pdf", plotTitle="", dpi=40):
    import matplotlib.pyplot as plt

    plt.figure()
    plt.plot(X)
    # plt.legend(methods)
    plt.title(plotTitle)
    # plt.ylim(0,1)
    # plt.axis('equal')
    plt.savefig(path, dpi=dpi)
    return


def mdTable(fileName, **columns):
    """
    prints a dicts as markdown table. The keys are used as head
    and the content of the list as body of the table's columns.
    The lists do not need to have identical length.
    """
    file = open(fileName, "w")
    headline = "|"
    separator = "|"
    for key in columns.keys():
        headline += key + "|"
        separator += "-|"

    file.write(headline + "\n")
    file.write(separator + "\n")
    n_rows = [len(columns[k]) for k in columns.keys()]

    for row in range(max(n_rows)):
        col_number = 0  # ColumNumber
        for key, value in columns.items():
            if row < n_rows[col_number]:
                file.write("| " + str(value[row]) + " ")
            else:
                file.write("| ")
            col_number += 1
        file.write("|\n")
    file.close()
