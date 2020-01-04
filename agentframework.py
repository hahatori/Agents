#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 22:05:27 2019

@author: tori
"""

import random

# Build the Agent class.
class Agent:
    
    # Define the initialization method to assign values of x and y.
    def __init__(self):
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)
        
    # Define the "move" method to change x and y randomly. 
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100 

            
# Creat objects, test the output random numbers y and x.             
a = Agent()
print(a.y, a.x)

a.move()
print(a.y, a.x)



