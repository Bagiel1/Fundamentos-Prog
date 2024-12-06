import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def f(x,y):
    return np.cos(x)*np.sin(y)

def gradiente_f(x, y):
    df_dx = -np.sin(x) * np.sin(y) 
    df_dy = np.cos(x) * np.cos(y)   
    return df_dx, df_dy

x = np.linspace(-np.pi, np.pi, 100)  
y = np.linspace(-np.pi, np.pi, 100)
x,y= np.meshgrid(x,y)
z= f(x,y)
df_x, df_y= gradiente_f(x,y)

fig= plt.figure(figsize=(20,8))

ax1= fig.add_subplot(131, projection='3d')
ax1.set_title("Função f(x,y)")
ax1.plot_surface(x,y,z, cmap='viridis')

ax2= fig.add_subplot(133)
contour= ax2.contourf(x, y, z, levels=50, cmap='hot')
fig.colorbar(contour, ax=ax2)
ax2.set_title("Curvas de Nível de f(x,y)")

ax3= fig.add_subplot(132)
ax3.quiver(x,y,df_x,df_y,color='blue', scale=40, headwidth=4, width=0.0015)
ax3.set_title("Gradiente da função")
ax3.contour(x,y,z, levels= 15, cmap='viridis')




plt.show()
