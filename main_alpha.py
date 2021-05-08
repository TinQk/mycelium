#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
import time


start_time = time.time()


## Constants

GRID_LENGTH = 5
GRID_WIDTH = 5

STEPS_NUMBER=10

## Run


grid = np.zeros((GRID_LENGTH, GRID_WIDTH))

all_cells = [ [2,2] ]



for i in range(STEPS_NUMBER):
        
    cell_grid = grid.copy()
    for cell in all_cells :
        
        
        theta = rd.randint(0,3)
        if theta == 0 :
            cell[0] += 1
        elif theta == 1 :
            cell[0] -= 1
        elif theta == 2 :
            cell[1] += 1
        else :
            cell[1] -=1
        
        cell_grid[cell[0],cell[1]] = 100
        
        print("theta = ", theta)
        print(all_cells)
        print(grid + cell_grid)
        
        input("")
        print ("\n" * 100) 

## Display

# print(grid + cell_grid)



end_time = time.time()

if __name__ == "__main__" :
    print("Execution time : ",end_time-start_time)
