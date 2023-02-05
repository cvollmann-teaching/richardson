from src.iterative_solver import richardson
from src import utils
import examples.example2 as conf


def main():
    sol, error, numit = richardson(conf.A, conf.b, conf.x0, theta=conf.theta, maxiter=conf.maxiter)
    print("error {error}\n"
          "iteration count {numit}\n"
          "maxiter {maxiter}".format(error=error[-1],
                                     numit=numit,
                                     maxiter=conf.maxiter))
    utils.plot1d(error, save_path="examples/out/conf1.pdf")
    utils.plot1d(sol, save_path="")
    return None

if __name__ == "__main__":
    main()

