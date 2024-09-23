import numpy as np
from matplotlib import pyplot as plt
import random
import time

b=[] #Responsável por armazenar os vetores 1
d=[] #Responsável por armazenar os vetores 2
c=[] #Responsável por armazenar os resultados
tempos=[] #Responsável por armazenar os tempos de cada operação


def vector(n): #Função que cria um vetor aleatório de n elementos
  return np.random.randint(-10,10,n)

z=random.randint(0,10) #Constante aleatória
w=random.randint(0,10) #Constante aleatória

b.extend([vector(10**5),vector(10**6),vector(10**7),vector(10**8)]) #Coloca dentro da lista b dos vetores os vetores criados aleatoriamente, vira uma lista de listas (matriz)
d.extend([vector(10**5),vector(10**6),vector(10**7),vector(10**8)]) #Mesma coisa so que na lista d 

p=[10**5,10**6,10**7,10**8] #So pra ficar mais fácil pro for percorrer
ka=[0,1,2,3] #Mesma coisa

for y,x in zip(ka,p): #Faz um for em que a duas variáveis se alteram juntas
  print("Para n igual a "+str(x)) #Printa qual a dimensão do vetor
  tempo_inicial= time.time() 
  resultado= b[y]*z+d[y]*w #Faz a operação chamando b[y] que é o vetor dentro de b: Se for 0, b[0] é o primeiro vetor dentro de b, nesse caso, vetor de dimensão 10**5
  c.append(resultado) #Coloca na lista c o resultado
  tempo_final= time.time() 
  tempo_total= tempo_final-tempo_inicial
  tempos.append(tempo_total) #Coloca na lista de tempos o tempo da operação
  print("Tempo de " +str(tempo_total)+"\n") #Printa o tempo


fig, (ax1,ax2)= plt.subplots(1,2,figsize=(14,6)) #Faz o plot

ax1.plot(p,tempos, marker='o')
ax1.set_xlabel('Tamanho de n')
ax1.set_ylabel('Tempo')
ax1.set_title('Escala Linear')

ax2.plot(p,tempos, marker='o')
ax2.set_xlabel('Tamanho de n')
ax2.set_ylabel('Tempo')
ax2.set_title('Escala semilog') 
ax2.set_xscale('log') #Coloca eixo x em log

plt.show()


