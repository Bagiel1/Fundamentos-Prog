import numpy as np

A= np.array([[1,0,0],[0,2,0],[0,0,3]])
xol= np.random.uniform(1,10,3)
xold= xol/np.linalg.norm(xol)


for i in range(1000):
  y= A @ xold

  xnew= y/np.linalg.norm(y)

  lambd = np.dot(xnew, A @ xnew)

  xold = xnew

print(lambd)


a= np.random.uniform(0,1,3)
B= np.diag(a)

for i in range(1000):
  y= B @ xold

  xnew= y/np.linalg.norm(y)

  lambd= np.dot(xnew, B @ xnew)

  xold = xnew

print(B)
print(lambd)
