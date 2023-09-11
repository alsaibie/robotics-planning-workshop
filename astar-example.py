import matplotlib.pyplot as plt
import numpy as np

# Define the grid 
grid_size = 9
grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

delta = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

# define start and goal
start = (0, 0)
goal = (8, 8)

# initialize g, h, and f values for the grid
g_values = np.full((grid_size, grid_size), np.inf)
h_values = np.full((grid_size, grid_size), np.inf)
f_values = np.full((grid_size, grid_size), np.inf)
source = np.full((grid_size, grid_size, 2), -1)
# initialize g, h, and f values for the start node

g_values[start] = 0
dx = abs(start[0] - goal[0]); dy = abs(start[1] - goal[1])
# octile distance
h_values[start] = 10 * max(dx, dy) + 4 * min(dx, dy)
f_values[start] = g_values[start] + h_values[start]

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
        # check if the neighbor is valid (within grid and not an obstacle)
        if 0 <= x < 9 and 0 <= y < 9 and grid[x][y] == 0:
            cost = 14 if dx * dy != 0 else 10
            # check if the path through 'current' is better than the previous path
            if g_values[current] + cost < g_values[x, y]:
                g_values[x, y] = g_values[current] + cost
                h_values[x, y] = max(abs(x - goal[0]), abs(y - goal[1])) * 10 + min(abs(x - goal[0]), abs(y - goal[1])) * 4
                f_values[x, y] = g_values[x, y] + h_values[x, y]
                source[x, y] = current
                if (x,y) not in open_list:
                    open_list.append((x,y))

# Backtracking to find the final path
if current == goal:
    path = [goal]
    while current != start:
        current = tuple(source[current])
        path.append(current)
        
# Plotting
fig, ax = plt.subplots()

for i in range(grid_size):
    for j in range(grid_size):
        if grid[i][j] == 1:
            ax.add_patch(plt.Rectangle((j, grid_size - i - 1), 1, 1, color='black'))
        else:
            plt.text(j + 0.1, grid_size - i - 0.5, f'{g_values[i, j]:.0f}', ha='left', va='top', fontsize=6)
            plt.text(j + 0.9, grid_size - i - 0.5, f'{h_values[i, j]:.0f}', ha='right', va='top', fontsize=6)
            plt.text(j + 0.5, grid_size - i - 0.9, f'{f_values[i, j]:.0f}', ha='center', va='center', fontsize=6)
        if source[i, j][0] != -1:
            dx, dy = source[i, j][1] - j, source[i, j][0] - i
            plt.arrow(j + 0.5, grid_size - i - 0.2, -dx * 0.1, dy * 0.1, head_width=0.05, head_length=0.05, fc='blue', ec='blue')
# Highlighting the final path in green
for x, y in path:
    ax.add_patch(plt.Rectangle((y, grid_size - x - 1), 1, 1, color='green', alpha=0.3))

plt.xlim(0, grid_size)
plt.ylim(0, grid_size)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

    
