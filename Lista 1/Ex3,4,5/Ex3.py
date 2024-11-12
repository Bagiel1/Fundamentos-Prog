import numpy as np
import matplotlib.pyplot as plt
import random
import time

#Exercício 3,4,5

plt.figure(figsize=(24,16))
plt.subplot(1,2,1)

P= 10 #Determina quantos a's serão utilizados
N=50 #Determina quantos x's serão utilizados para cada valor de 'a'
a=[]
resultados= []
for _ in range(P): #Cria os valores de a aleatórios entre 0 e 4
  a.append(random.uniform(0,4))
a=sorted(a) #Organiza os valores de a em ordem crescente


for _ in range(P):
  x=0.1
  temp_result= [] #Cria uma lista temporária que vai ser colocada dentro dos resultados e resetada sempre que trocar o valor de 'a'
  for i in range(N):
    x= a[_]*x*(1-x) #Equação
    temp_result.append(x)
  resultados.append(temp_result)
  plt.plot(temp_result, label= f'{a[_]:.2f}', marker='o') 
  #Coloca o temp_result como eixo y e como eixo x o "Número de iterações" ou seja, o tamanho de "temp_result". Como não especificou o eixo x, o plt.plot cria automaticamente o eixo x como o tamanho do eixo y


#Faz a média para cada lista dentro da lista resultados
for _ in range(len(resultados)):
  media=0
  for i in range(len(resultados[0])):
    media= resultados[_][i] + media
  media= media/len(resultados[0])
  print(f"A média do índice {_} é {media}")

  #Faz a variança para cada lista dentro da lista resultados
  varianca=0
  for i in range(len(resultados[0])):
    varianca= (resultados[_][i]-media)**2 + varianca
  varianca= varianca/(len(resultados[0])-1)
  print(f"A variança do índice {_} é {varianca}")
  #Agora ele faz a mesma coisa so que com numpy
  print(f"Para índice {_} a média no numpy é {np.mean(resultados[_])}")
  print(f"Para índice {_} a variança no numpy é {np.var(resultados[_],ddof=1)}")


#Organiza o gráfico
plt.title("Mapeamento Logístico: Sequência para diferentes valores de a")
plt.xlabel("Iterações")
plt.ylabel("Valor de X")
plt.legend(fontsize='small', loc= 'upper left')
plt.grid(True)  


#Exercício 5 começa aqui 
plt.subplot(1,2,2) #Plota outro gráfico do lado

N=1000
M=1 #Um número mínimo de iterações para os x's se estabilizarem
x= 0.1
a= np.linspace(0,4,1000) #Criar 1000 a's de 0 a 4 com distâncias iguais
temp_res= []
result= []

for ax in a:
    x= 0.1
    for i in range(N):
      x= x*ax*(1-x)
      if(i>=M): #Somente se for maior que a quantidade determinada será append, pois já estará estabilizado
        result.append((ax,x)) 
#Plota duplas, ax (sendo a) e x (sendo um número de x) --> Do formato (1,0.4). Como os x's já estão estabilizados então, por exemplo, antes do a=3 ficará sempre a mesma dupla: (1,0.4) - (1,0.4) - ... 
#e isso mostrará então, no gráfico, um único ponto
      
result= np.array(result)

plt.plot(result[:,0],result[:,1], ',k') #Result[:,0] significa que to chamando todos os 'as' de todas as duplas e [:,1] todos os x's 
plt.tight_layout()
plt.show()
