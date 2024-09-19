import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

n= 100

p0, p1= 0.7,0.3

grid= np.random.choice([0,1],100*100, p=[p0,p1]).reshape(n,n)


def update(frameNum, img, grid):

    new_grid= grid.copy()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            quantidade= 0
            if j > 0:
                quantidade += grid[i][j-1]
            if j < n-1:
                quantidade += grid[i][j+1]
            if i > 0:
                quantidade += grid[i-1][j]
            if i < n-1:
                quantidade += grid[i+1][j]
            if i > 0 and j > 0:
                quantidade += grid[i-1][j-1]
            if i > 0 and j < n-1:
                quantidade += grid[i-1][j+1]
            if i < n-1 and j < n-1:
                quantidade += grid[i+1][j+1]
            if i < n-1 and j > 0:
                quantidade += grid[i+1][j-1]

            if grid[i][j]==0:

                if quantidade == 3:
                    new_grid[i][j] = 1
                else:
                    new_grid[i][j] = 0
        
            elif grid[i][j]==1:
                if quantidade < 2:
                    new_grid[i][j]=0
                elif quantidade >= 2 and quantidade <= 3:
                    new_grid[i][j]=1
                elif quantidade > 3:
                    new_grid[i][j]=0

    img.set_data(new_grid)
    grid[:]= new_grid[:]
    plt.title(f"Game of Life - Frame {frameNum}")
    return img,

print(grid[1][2])

fig, ax= plt.subplots()
img = ax.imshow(grid,interpolation='nearest')
ani = animation.FuncAnimation(fig,update,fargs=(img,grid), interval=10)
plt.show()

