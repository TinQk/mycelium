#! /usr/bin/env python3
# -*- coding: utf-8 -*-

## Built in modules

import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
import time
import matplotlib.cm as cm

import os
import sys


## Project modules

main_dir_path = os.getcwd()
modules_path = main_dir_path + "\\modules"

# On ajoute le dossier modules aux dossiers de recherche des modules
if modules_path not in sys.path:
    sys.path.append(modules_path)

import map_modules
import params



def main():
    start_time = time.time()
    
    ## Run
    
    # Map creation
    m = map_modules.Map(params.MAP_LENGTH, params.MAP_WIDTH)
    m.add_obstacles(params.OBSTACLES)
    
    map = m.grid


    

    # Cells creation
    all_cells = [ [2,2] ,  [3,3], [7,6], [7,6], [9,9] ]
    
    def accessible(x,y) :        
        return not (x<0 or y<0 or x >= params.MAP_LENGTH or y>=params.MAP_WIDTH or map[x,y] == params.WALLS_VALUE)

        
    for i in range(params.STEPS_NUMBER):
            
        cell_map = np.zeros((params.MAP_LENGTH, params.MAP_WIDTH))
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
        
        print(all_cells)
        print(map + cell_map)
            
        input("")
        print ("\n" * 100) 
        
        
        ## Save sim as images
        
        if params.SAVE_SIM:
            fig, ax = plt.subplots()
            # ax.imshow(map + cell_map, interpolation='bilinear', cmap=cm.Greys_r)
            ax.imshow(map + cell_map, interpolation='nearest', cmap=cm.Greys_r)
            fig.savefig("{:04d}".format(i))
            fig.clear()
        
        

 
   
    ## End
    
    end_time = time.time()
    if __name__ == "__main__" :
        print("Execution time : ",end_time-start_time)


## Run

if __name__ == "__main__":
    main()



