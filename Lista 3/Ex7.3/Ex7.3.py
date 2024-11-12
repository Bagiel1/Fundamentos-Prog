import numpy as np

A= np.array([[1,0,0],[0,2,0],[0,0,3]])
xol= np.array([1,5,10])
xold= xol/np.linalg.norm(xol)


for i in range(1000):
  y= A @ xold

  xnew= y/np.linalg.norm(y)

  lambd = np.dot(xnew, A @ xnew)

  xold = xnew

print(lambd)
