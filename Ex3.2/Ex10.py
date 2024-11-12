import numpy as np
import random
from matplotlib import pyplot as plt

def integral():
  n=[10,10**2,10**3,10**4]
  pi_estimado= []
  for i in n:
    x= np.linspace(0,1,i)
    soma=0
    xm= np.array([])
    for i in range(i-1):
      xm=np.append(xm, (x[i]+x[i+1])/2)
    for i in range(i-1):
      y= ((1-(xm[i])**2)**(1/2)) * (x[i+1]-x[i])
      soma+=y
    pi_estimado.append(soma*4)

  dif= [(np.pi - pi_estimado[i]) for i in range(len(pi_estimado))]

  plt.plot(n, dif, marker='o')
  plt.xscale('log')
  plt.yscale('log')
  plt.xlabel('N')
  plt.ylabel('Diferença do pi estimado com o seu valor real')
  plt.grid(True)
  plt.show()

integral()