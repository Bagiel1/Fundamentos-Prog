import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

N=100

def criarGrade(N):
    p0,p1= 0.6,0.4
    A= np.random.choice([0,2], N*N, p=[p0, p1]).reshape(N, N)
    return A

metade= N//2
grid= criarGrade(N)
grid[metade,metade]= 1

cmap = ListedColormap(['white', 'blue', 'black'])

def update(frameNum, img, grid):

    new_grid = grid.copy()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i,j] == 1:
                if j > 0 and grid[i][j-1] == 0:
                    new_grid[i][j-1] = 1
                if j < N-1 and grid[i][j+1] == 0:
                    new_grid[i][j+1] = 1  
                if i > 0 and grid[i-1][j] == 0:
                    new_grid[i-1][j] = 1  
                if i < N-1 and grid[i+1][j] == 0:
                    new_grid[i+1][j] = 1


    img.set_data(new_grid)
    grid[:] = new_grid[:]

    plt.title(f"Flooding - Frame: {frameNum}")
    
    return img,

fig, ax = plt.subplots()

img = ax.imshow(grid, cmap= cmap, interpolation='nearest')

ani = animation.FuncAnimation(fig, update, fargs=(img, grid), interval=10)

plt.show()

