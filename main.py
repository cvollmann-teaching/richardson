from src.iterative_methods import richardson
from src import utils
import examples.pagerank_small as conf


def main():
    sol, error, numit = richardson(
        conf.A, conf.b, conf.x0, theta=conf.theta, maxiter=conf.maxiter
    )
    print(
        "error {error}\n"
        "iteration count {numit}\n"
        "maxiter {maxiter}".format(error=error[-1], numit=numit, maxiter=conf.maxiter)
    )
    utils.plot1d(error, save_path="examples/out/conf1.pdf")
    utils.plot1d(sol, save_path="")
    return sol, error, numit


if __name__ == "__main__":
    sol, error, numit = main()
