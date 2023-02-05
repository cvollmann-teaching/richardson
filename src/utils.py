def plot2d_iterates(X, save_path="out/2diterates.pdf", dpi=400):
    import matplotlib.pyplot as plt
    plt.figure()
    for i in range(len(X)):
        plt.plot(X[i][0], X[i][1], "ro--")
    # plt.legend(methods)
    plt.title("Iterates x_k")
    plt.axis('equal')
    if save_path:
        plt.savefig(save_path, dpi=dpi)
    return


def plot1d(X, save_path="out/1d.pdf", plotTitle="", dpi=40):
    import matplotlib.pyplot as plt
    plt.figure()
    plt.plot(X)
    # plt.legend(methods)
    plt.title(plotTitle)
    # plt.ylim(0,1)
    # plt.axis('equal')
    if save_path:
        plt.savefig(save_path, dpi=dpi)
    return
