import numpy as np
import random
from matplotlib import pyplot

def integral(n):
  x= np.linspace(0,1,n)
  soma=0
  xm= np.array([])
  for i in range(n-1):
    xm=np.append(xm, (x[i]+x[i+1])/2)
  for i in range(n-1):
    y= ((1-(xm[i])**2)**(1/2)) * (x[i+1]-x[i])
    soma+=y
  return soma*4

print(integral(1000))