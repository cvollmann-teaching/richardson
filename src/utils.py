def plot2d_iterates(X, save_path="out/2diterates.pdf", dpi=400):
    import matplotlib.pyplot as plt

    plt.figure()
    for i in range(len(X)):
        plt.plot(X[i][0], X[i][1], "ro--")
    # plt.legend(methods)
    plt.title("Iterates x_k")
    plt.axis("equal")
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


class callback_iterates:
    def __init__(self, disp=True):
        self.iterates = []

    def __call__(self, other):
        self.iterates += [other]


def save_1d_gif(iterates: list, save_path: str, **kwargs):
    import numpy as np
    from matplotlib.animation import FuncAnimation
    import matplotlib.pyplot as plt

    numiter = len(iterates)
    frames = zip(iterates, list(range(len(iterates))))
    grid = np.linspace(0, 1, len(iterates[0]))
    fig = plt.figure()
    ax = plt.axes(xlim=(0, 1), ylim=(0, 0.15))
    (line,) = ax.plot([], [], lw=2)

    def init():
        line.set_data([], [])
        return (line,)

    def func(frame):
        iterate, it = frame
        iterate[0] = 0
        iterate[-1] = 0
        line.set_data(grid, iterate)
        return (line,)

    anim = FuncAnimation(
        fig,
        func,
        init_func=init,
        frames=frames,
        interval=300,
        save_count=numiter,
        repeat_delay=2000,
    )
    fig.suptitle("heat equation")
    anim.save(save_path, writer="imagemagick")
    return None
