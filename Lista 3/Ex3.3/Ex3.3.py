import numpy as np
import matplotlib.pyplot as plt

y= np.random.uniform(0,100)
x= np.random.uniform(0,100)

def Jacobi(TOL,x,y):

  n= 0
  xs = []
  ys = []
  while abs(3*x-y-2) >= TOL:
    x_= 1/3*(2+y)
    y_= 1/4*(1+2*x)
    x= x_
    y=y_
    xs.append(x)
    ys.append(y)
    n+=1

  return n



TOLS= [1e-2,1e-3,1e-4,1e-5,1e-6,1e-7,1e-8]
ns= []
for i in TOLS:
  b=Jacobi(i,x,y)
  ns.append(b)

print(ns)

plt.plot(ns, TOLS)
plt.show()