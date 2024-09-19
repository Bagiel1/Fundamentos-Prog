import numpy as np
from matplotlib import pyplot as plt
import random
import time

#Pegar matriz randômica NxN e calcular sua M potência

p=[1000,2000,3000,4000]
q=[2,3,4]
j=[0,1,2,3]
a=[]
tempos2= []
tempos3=[]
tempos4=[]


#Inicializo as matrizes e coloco elas na lista a[]
def matrix(n):
    return np.random.randint(-10,10,size=(n,n))
for n in p:
    a.append(matrix(n))
print(a[0])

def mult(m,matriz):
    original,resultado= matriz,matriz
    for i in range(1,m):
        resultado= np.matmul(resultado,original)
    return resultado

for x,w in zip(j,p):
    print("Para n igual a "+str(w))
    for y in q:
        tempo_inicial= time.time()
        print("Para m igual a "+str(y))
        mult(y,a[x])
        tempo_final= time.time() - tempo_inicial
        print("Tempo necessário: "+str(tempo_final))
        if y == 2:
            tempos2.append(tempo_final)
        elif y == 3:
            tempos3.append(tempo_final)
        elif y == 4:
            tempos4.append(tempo_final)


#Matplotlib

fig, (ax1,ax2)= plt.subplots(1,2,figsize=(14,6))

ax1.plot(p,tempos2, marker='o', label="m=2")
ax1.plot(p,tempos3,marker='o',label="m=3")
ax1.plot(p,tempos4,marker='o',label="m=4")
ax1.grid(True)
ax1.set_xlabel("Dimensão")
ax1.set_ylabel("Tempo")
ax1.set_title("Escala Linear dos tempos necessários para o programa funcionar")

ax2.plot(p,tempos2, marker='o', label="m=2")
ax2.plot(p,tempos3,marker='o',label="m=3")
ax2.plot(p,tempos4,marker='o',label="m=4")
ax2.grid(True)
ax2.set_xscale('log')
ax2.set_xlabel("Dimensão")
ax2.set_ylabel("Tempo")
ax2.set_title("Escala Log dos tempos necessários para o programa funcionar")

plt.show()


