import numpy as np

class Environment:
    def __init__(dims):
        # create the array of ants, containing their intensive properties such as
        # energy level and internal state variables
        # create the world and set its spatial variables
        self.world = np.zeros(dims, dtype=[('pheromone', np.float64),('food', np.float64)])

    def step():
        pass



def main():
    size = 500
    dims = (size, size)
    env = Environment(dims)


if __name__ == '__main__':
    main()
