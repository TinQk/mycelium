import numpy as np


### PARAMETERS

N = 100 # Universe size (height and width)
T = 5000 # Time limit

class Universe:

    def __init__(self, size, time_limit, time = 0):
        self.size = size 
        self.time_limit = time_limit
        self.time = time
        self.structure = self.create_structure()

    def create_structure(self):
        struct = - np.ones((self.time_limit, self.size, self.size))
        struct[:, 1:-1, 1:-1] = np.zeros((self.time_limit, self.size - 2, self.size - 2))
        return struct

    def populate(self):
        for i in range(self.size) :
            for j in range(self.size) :
                if self.structure[0,i,j] != -1 :
                    nb = np.random.rand()
                    if nb < 0.05 :
                        self.structure[0,i,j] = 1
                        #Cells.append([1,(i,j),5,1,1,1])
                    elif 0.99 < nb :
                        self.structure[0,i,j] = 3
                        #Cells.append([3,(i,j),300,1,1,1])
                    elif  0.05 < nb < 0.06 :
                        #Cells.append([2,(i,j),5,1,1,1])
                        pass

    def get_entity(self, x, y):
        return self.structure[self.time, x, y]

class Cell:
    def __init__(self, universe, position):
        self.universe = universe
        self.position = position

    def get_adjacent_cells(self):
        adjacents = []
        if self.x > 0:
            adjacents.append(self.universe.get_entity(self.x - 1, self.y))
        if self.x < self.universe.size - 1:
            adjacents.append(self.univers.get_entity(self.x + 1, self.y))
        if self.y > 0:
            adjacents.append(self.univers.get_entity(self.x, self.y - 1))
        if self.y < self.universe.size - 1:
            adjacents.append(self.univers.get_entity(self.x, self.y + 1))
        return adjacents

    
class Predator(Cell):
    def move(self):
        pass

    def eat(self):
        pass


class CellFeature:
    def __init__(self):
        pass



if __name__ == "__main__":
    # Create Universe
    univ = Universe(N, T)
    print("Shape : ", univ.structure.shape)
    print("virgin universe t=0 : \n", univ.structure[0, :, :], "\n")
    print("virgin universe t=5 : \n", univ.structure[5, :, :], "\n")
    print("virgin universe t=-1 : \n", univ.structure[-1, :, :], "\n")
    
    # Populate Universe
    univ.populate()
    print("Populated universe t=0 : \n", univ.structure[0, :, :], "\n")

    # Start time
