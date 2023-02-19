from src.iterative_methods import richardson
from src import utils
import examples.heat_equation as conf
from src.pagerank_utils import callback_iterates
from src.pagerank_utils import save_pagerank_gif
from src.utils import save_1d_gif


def main(save_path=None):
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
    if save_path:
        # save_pagerank_gif(
        #     conf.filename,
        #     callback.iterates,
        #     save_path=conf.save_path,
        #     damping_factor=conf.alpha,
        # )
        save_1d_gif(callback.iterates[::100], save_path=conf.save_path)
    return sol, error, numit, callback


if __name__ == "__main__":
    sol, error, numit, callback = main(save_path=conf.save_path)
