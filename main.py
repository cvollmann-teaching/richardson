from src.iterative_methods import richardson
from src import utils
import examples.pagerank_small as conf
from src.pagerank_utils import callback_iterates
from src.pagerank_utils import save_pagerank_gif


def main():
    callback = callback_iterates()
    sol, error, numit = richardson(
        conf.A,
        conf.b,
        conf.x0,
        theta=conf.theta,
        maxiter=conf.maxiter,
        callback=callback,
    )
    print(
        "error {error}\n"
        "iteration count {numit}\n"
        "maxiter {maxiter}".format(error=error[-1], numit=numit, maxiter=conf.maxiter)
    )
    utils.plot1d(error, save_path="examples/out/conf1.pdf")
    utils.plot1d(sol, save_path="")
    return sol, error, numit, callback


if __name__ == "__main__":
    sol, error, numit, callback = main()
    save_pagerank_gif(
        conf.filename,
        callback.iterates,
        save_path="examples/out/pagerank_small.gif",
        damping_factor=conf.alpha
    )
