import numpy as np


### PARAMETERS

N = 10 # Universe size (height and width)
T = 50 # Time limit

class Universe:

    def __init__(self, size, time_limit):
        self.size = size 
        self.time_limit = time_limit
        self.structure = self.create_structure()

    def create_structure(self):
        struct = - np.ones((self.time_limit, self.size, self.size))
        struct[:, 1:-1, 1:-1] = np.zeros((self.time_limit, self.size - 2, self.size - 2))
        return struct






if __name__ == "__main__":
    # Create Universe
    univ = Universe(N, T)
    print(univ.structure[0, :, :])
    print(univ.structure[5, :, :])
    print(univ.structure[-1, :, :])

    # Populate Universe

    # Start time
