import numpy as np
from matplotlib import pyplot as plt
import random
import time

dimens= [1,2,3,4]
temposNp= []
temposPy= []

#Crio as matrizes com list comprehension para cada dimensão, ou seja, isso cria matrizes de todas as combinações... 200x200, 200x300, 200x400, 300x200 etc...
for n in dimens:
    for p in dimens:
        matrizA= [[random.randint(0,10) for _ in range(n)] for _ in range(n)] #O for de dentro indica a quantidae de colunas que terá, e o for de fora a quantidade de linhas
        matrizB= [[random.randint(0,10) for _ in range(p)]  for _ in range(p)] #Só criar matrizes quadradas
    

        if n==p: #Verifica se a quantidade de colunas da matrizA é igual a quantidade de linhas da matrizB
            resultado= [[0]*p for _ in range(n)] #Crio o resultado que é uma matriz de zeros (por enquanto) com a quantidade de linhas da primeira matriz e colunas da segunda
            tempoinicial= time.time()
            for i in range(n): #Percorre as linhas da matrizA
                for j in range(n): #Percorre as linhas da matrizB
                    soma=0 
                    for k in range(n): #Serve para deslocar os numeros da linha fixada da matrizA e da coluna fixada da matrizB
                        soma+=matrizA[i][k]*matrizB[k][j]
                    resultado[i][j]= soma #Atribuo o resultado à soma
            tempofinal= time.time() - tempoinicial
            temposPy.append(tempofinal)
            matrizA= np.array(matrizA) #Transformo em array do numpy para poder fazer as ações do numpy
            matrizB= np.array(matrizB)
            tempoinicial= time.time()
            resultado= matrizA@matrizB #Multiplicação numpy
            tempofinal= time.time() - tempoinicial
            temposNp.append(tempofinal) 

#Ploto no gráfico, sendo x as dimensões e y os tempos de ambos

plt.plot(dimens, temposPy, marker='o', label='Tempos Python')
plt.plot(dimens, temposNp, marker='o', label='Tempos Numpy')
plt.legend()
plt.show()
