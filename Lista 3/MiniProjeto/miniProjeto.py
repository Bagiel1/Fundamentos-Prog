import numpy as np
from scipy.integrate import quad

N=10
L= 1
Tensao= 2
Lo= L/N
posicao= []
tensao= []
massas= []
pesos= []
iniciais=[]
ysold = np.random.rand(9)
ysold = np.insert(ysold, 0, 0)
ysold = np.append(ysold, 0)
g= 10




def forcas(n):
  for i in range(n):
    iniciais.append(0)
forcas(N-1)

def rho(x):
  return 1

for i in range(N-1):
  if i == 0:
    a= 0
    b= 3*Lo/2
  elif i == N-2:
    a= L - 3*Lo/2
    b= L
  else:
    a= (i+1)*Lo-Lo/2
    b= (i+1)*Lo+Lo/2

  massa, er= quad(rho, a, b)
  massas.append(round(massa,2))
  peso= massa * g
  pesos.append(round(peso,2))

print(iniciais)
print(pesos)
print(massas)


for i in range(0,N-1):
  matrizresultado= [massas[i]*g - iniciais[i]]