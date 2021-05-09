#! /usr/bin/env python3
# -*- coding: utf-8 -*-

## Built in modules

import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
import time

import os
import sys



## Project modules

main_dir_path = os.getcwd()
modules_path = main_dir_path + "\\modules"

# On ajoute le dossier modules aux dossiers de recherche des modules
if modules_path not in sys.path:
    sys.path.append(modules_path)

import map_modules


## Constants

MAP_LENGTH = 10
MAP_WIDTH = 10
OBSTACLES = [[0, 0], [1,0], [1,1], [2,0], [0,2]]

STEPS_NUMBER=100




def main():
    start_time = time.time()
    
    ## Run
    
    # Map creation
    m = map_modules.map(MAP_LENGTH, MAP_WIDTH)
    m.add_obstacles(OBSTACLES)
    
    map = m.grid
    

    # Cells creation
    all_cells = [ [2,2] ,  [3,3], [7,6], [7,6], [9,9] ]
    
    def accessible(x,y) :        
        return not (x<0 or y<0 or x >= MAP_LENGTH or y>=MAP_WIDTH or map[x,y] == -1)
        
    for i in range(STEPS_NUMBER):
            
        cell_map = np.zeros((MAP_LENGTH, MAP_WIDTH))
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
            
            print("theta = ", theta)
        
        
        ## Display   
        
        print(all_cells)
        print(map + cell_map)
            
        input("")
        print ("\n" * 100) 
 
   
    ## End
    
    end_time = time.time()
    if __name__ == "__main__" :
        print("Execution time : ",end_time-start_time)


## Run

if __name__ == "__main__":
    main()



