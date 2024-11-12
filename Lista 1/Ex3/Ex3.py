import numpy as np
import matplotlib.pyplot as plt
import random
import time

#Exercício 3,4 e 5 aqui

plt.figure(figsize=(24,16))
plt.subplot(1,2,1)

P= 10 #Determina quantos a's serão aleatorizados
N= 50 #Determina quantos x's vão ser atribuídos
a=[] 
resultados= []
for _ in range(P): #Cria "a's" aleatórios entre 0 e 4
  a.append(random.uniform(0,4))
print("Numeros a")
a=sorted(a) #Coloca os a's em ordem crescente


for _ in range(P):
  x=0.1
  temp_result= [] #Cria uma lista temporária que vai ser transporatada para os resultados
  for i in range(N):
    x= a[_]*x*(1-x) #Para um 'a' específico, terá a sequência logística, depois trocará o 'a'
    temp_result.append(x)
  resultados.append(temp_result)
  plt.plot(temp_result, label= f'{a[_]:.2f}', marker='o') 
print(resultados)
plt.show()
'''


for _ in range(len(resultados)):
  media=0
  for i in range(len(resultados[0])):
    media= resultados[_][i] + media
  media= media/len(resultados[0])
  print(media)


  varianca=0
  for i in range(len(resultados[0])):
    varianca= (resultados[_][i]-media)**2 + varianca
  varianca= varianca/(len(resultados[0])-1)
  print(varianca)

  print(np.mean(resultados[_]))
  print(np.var(resultados[_],ddof=1))



plt.title("Mapeamento Logístico: Sequência para diferentes valores de a")
plt.xlabel("Iterações")
plt.ylabel("Valor de X")
plt.legend(fontsize='small', loc= 'upper left')
plt.grid(True)  


plt.subplot(1,2,2)

N=1000
M=100
x= 0.1
a= np.linspace(0,4,1000)
temp_res= []
result= []

for ax in a:
    x= 0.1
    for i in range(N):
      x= x*ax*(1-x)
      if(i>=M):
        result.append((ax,x))
      
    

result= np.array(result)

plt.plot(result[:,0],result[:,1], ',k')
plt.tight_layout()
plt.show()
'''