import numpy as np

n= 2
A= np.random.rand(n,n)
B= np.array([[3,-1], [-2,4]])

O= np.diag(np.diag(B))

L= np.tril(B, -1)
U= np.triu(B, 1)

b= np.array([2,1])
iter=0
maxit= 1000
tol= 1e-5
err= 10*tol
xold= np.random.rand(n)
while(iter<maxit and err > tol):
  xnew= np.linalg.inv(O)@(b-(L+U)@xold)
  err= np.linalg.norm(xnew-xold)
  print(iter, err)
  iter += 1
  xold = xnew
print(xnew)