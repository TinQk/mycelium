#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
import time


start_time = time.time()


## Constants

GRID_LENGTH = 10
GRID_WIDTH = 10

STEPS_NUMBER=100


## Run


grid = np.zeros((GRID_LENGTH, GRID_WIDTH))
grid[0,0] = -1
grid[1,0] = -1
grid[0,1] = -1
grid[1,1] = -1
grid[2,0] = -1
grid[0,2] = -1


all_cells = [ [2,2] ,  [3,3], [7,6], [7,6], [9,9] ]

def possible(x,y) :        
    return not (x<0 or y<0 or x >= GRID_LENGTH or y>=GRID_WIDTH or grid[x,y] == -1)
    
for i in range(STEPS_NUMBER):
        
    cell_grid = np.zeros((GRID_LENGTH, GRID_WIDTH))
    for cell in all_cells :
        
        b = True
        while b :
            b = False
            theta = rd.randint(4)
            if theta == 0 :
                if possible(cell[0]+1,cell[1]) :
                    cell[0] += 1
                else :
                    b = True
            elif theta == 1 :
                if possible(cell[0]-1,cell[1]) :
                    cell[0] -= 1
                else :
                    b = True
            elif theta == 2 :
                if possible(cell[0],cell[1]+1) :
                    cell[1] += 1
                else :
                    b = True
            else :
                if possible(cell[0],cell[1]-1) :
                    cell[1] -= 1
                else :
                    b = True
                
        cell_grid[cell[0],cell[1]] += 100
        
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
