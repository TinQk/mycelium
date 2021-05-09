#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
import time
import matplotlib.cm as cm
import os

print(os.getcwd())

## Constants

map_LENGTH = 10
map_WIDTH = 10

STEPS_NUMBER=100

WALLS_VALUE = -100


def main():
    start_time = time.time()
    
    ## Run
    
    # Map creation
    map = np.zeros((map_LENGTH, map_WIDTH))
    
    # Obstacles
    map[0,0] = WALLS_VALUE
    map[1,0] = WALLS_VALUE
    map[0,1] = WALLS_VALUE
    map[1,1] = WALLS_VALUE
    map[2,0] = WALLS_VALUE
    map[0,2] = WALLS_VALUE
    
    # Cells creation
    all_cells = [ [2,2] ,  [3,3], [7,6], [7,6], [9,9] ]
    
    def accessible(x,y) :        
        return not (x<0 or y<0 or x >= map_LENGTH or y>=map_WIDTH or map[x,y] == WALLS_VALUE)
        
    for i in range(STEPS_NUMBER):
            
        cell_map = np.zeros((map_LENGTH, map_WIDTH))
        for cell in all_cells :
            
            b = True
            while b :
                b = False
                theta = rd.randint(4)
                if theta == 0 :
                    if accessible(cell[0]+1,cell[1]) :
                        cell[0] += 1
                    else :
                        b = True
                elif theta == 1 :
                    if accessible(cell[0]-1,cell[1]) :
                        cell[0] -= 1
                    else :
                        b = True
                elif theta == 2 :
                    if accessible(cell[0],cell[1]+1) :
                        cell[1] += 1
                    else :
                        b = True
                else :
                    if accessible(cell[0],cell[1]-1) :
                        cell[1] -= 1
                    else :
                        b = True
                    
            cell_map[cell[0],cell[1]] += 100
          
          
          
        
        ## Display   
                    
        fig, ax = plt.subplots()
        # ax.imshow(map + cell_map, interpolation='bilinear', cmap=cm.Greys_r)
        ax.imshow(map + cell_map, interpolation='nearest', cmap=cm.Greys_r)
        fig.savefig("{:04d}".format(i))
        fig.clear()
        
        
        # print(all_cells)
        # print(map + cell_map)
            
        # input("")
        # print ("\n" * 100) 
 
   
    ## End
    
    end_time = time.time()
    if __name__ == "__main__" :
        print("Execution time : ",end_time-start_time)


## Run

if __name__ == "__main__":
    main()



