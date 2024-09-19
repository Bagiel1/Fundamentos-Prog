import numpy as np
from matplotlib import pyplot as plt
import random
import time

b=[]
d=[]
c=[]
tempos=[]


def matrix(n):
  return np.random.randint(-10,10,n)

z=random.randint(0,10)
w=random.randint(0,10)

b.extend([matrix(10**5),matrix(10**6),matrix(10**7),matrix(10**8)])
d.extend([matrix(10**5),matrix(10**6),matrix(10**7),matrix(10**8)])

p=[10**5,10**6,10**7,10**8]
ka=[0,1,2,3]

for y,x in zip(ka,p):
  print("Para n igual a "+str(x))
  tempo_inicial= time.time()
  resultado= b[y]*z+d[y]*w
  c.append(resultado)
  tempo_final= time.time()
  tempo_total= tempo_final-tempo_inicial
  tempos.append(tempo_total)
  print("Tempo de " +str(tempo_total)+"\n")


fig, (ax1,ax2)= plt.subplots(1,2,figsize=(14,6))

ax1.plot(p,tempos, marker='o')
ax1.set_xlabel('Tamanho de n')
ax1.set_ylabel('Tempo')
ax1.set_title('Escala Linear')

ax2.plot(p,tempos, marker='o')
ax2.set_xlabel('Tamanho de n')
ax2.set_ylabel('Tempo')
ax2.set_title('Escala semilog')
ax2.set_xscale('log')

plt.show()


