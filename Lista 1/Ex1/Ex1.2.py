import numpy as np
from matplotlib import pyplot as plt
import random
import time

#Pegar matriz randômica NxN e calcular sua M potência

p=[100,200,300,400] #Dimensões da matriz
q=[2,3,4] #Potência que a matriz vai ficar
j=[0,1,2,3] #Auxiliar ao for
a=[] #Lista onde as matrizes vao ficar
tempos2= [] #Tempos da potência 2
tempos3=[] #Tempos da potência 3
tempos4=[] #Tempos da potência 4


#Inicializo as matrizes e coloco elas na lista a[]
def matrix(n):
    return np.random.randint(-10,10,size=(n,n))
for n in p:
    a.append(matrix(n))

#Função para fazer a potencia da matriz
def mult(m,matriz):
    original,resultado= matriz,matriz 
    for i in range(1,m):
        resultado= np.matmul(resultado,original)
    return resultado

#Loop for dentro de loop for, o primeiro percorre as matrizes e, para cada matriz ele faz a potência (2,3,4) dessa matriz, depois troca a matriz
for x,w in zip(a,p):
    print("Para n igual a "+str(w))
    for y in q:
        print("Para m igual a "+str(y))
        tempo_inicial= time.time()
        mult(y,x) #Chama a função de potencia
        tempo_final= time.time() - tempo_inicial
        print("Tempo necessário: "+str(tempo_final))
        #Verifica qual é a potência atual para armazenar em uma lista específica da potência
        if y == 2:
            tempos2.append(tempo_final)
        elif y == 3:
            tempos3.append(tempo_final)
        elif y == 4:
            tempos4.append(tempo_final)


#Matplotlib

#Plota 2 gráficos, um linear e o outro log, com 3 linhas distintas, uma para cada potência

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


