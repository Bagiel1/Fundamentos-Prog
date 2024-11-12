import numpy as np

x= np.random.uniform(0,100)
y= np.random.uniform(0,100)
z= np.random.uniform(0,100)
TOL= 1e-100

while abs(3*x-y-z-1) >= TOL  and abs(-x+3*y-z-2) >= TOL and abs(-x-y+3*z-3) >= TOL:
  x_= (y+z+1)/3
  y_= (x+z+2)/3
  z_= (x+y+3)/3

  x,y,z= x_,y_,z_

print(x)
print(y)
print(z)


print(3*x-y-z)