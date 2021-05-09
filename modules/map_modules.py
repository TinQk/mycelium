#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

class map:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.grid = np.zeros((length, width))
        
    
    def add_obstacles(self, obs_locations):
        for loc in obs_locations:
            self.grid[loc[0], loc[1]] = -1
