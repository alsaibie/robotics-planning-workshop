import matplotlib.pyplot as plt
import numpy as np

# Define the grid 
grid_size = 9
# grid = 

delta = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
# define start and goal
# start =
# goal = 

# initialize g, h, and f values for the grid
# ...
# initialize g, h, and f values for the start node
# ...
# A* algorithm
open_list = [start]
while open_list:
    # find the node with the lowest f value
    current = min(open_list, key=lambda x: f_values[x])
    if current == goal:
        print("Goal found!")
        break
    open_list.remove(current)
    
    # check all the neighbors of 'current'
    for dx, dy in delta:
        x, y = current[0] + dx, current[1] + dy
        # ..

# Backtracking to find the final path
if current == goal:
    path = [goal]
    while current != start:
        current = tuple(source[current])
        path.append(current)
        

    
