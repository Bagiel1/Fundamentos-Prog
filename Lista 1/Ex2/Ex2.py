import numpy as np
from matplotlib import pyplot
import random
import time
from matplotlib import pyplot as plt


#Usando so as funções do pyton=
MatrizR=[] #Armazenas os resultados
dimensoes=[50,100,200,300] 
temposNP= []
temposPy= []
linhas_matriz_A = []
colunas_matriz_B = []


def criar(n,j,p,q):
    matrizA= [[random.randint(0,5) for i in range(j)] for _ in range(n)] #List comprehension
    matrizB= [[random.randint(0,5) for i in range(q)] for _ in range(p)]
    print("As dimensões escolhidas foram: "+str(n) +"x" +str(j) +" e " +str(p) +"x" +str(q))
    return matrizA,matrizB

def mult(matriz1, matriz2):

    linhas1= len(matriz1)
    colunas1= len(matriz1[0])
    linhas2= len(matriz2)
    colunas2= len(matriz2[0])

    if colunas1 != linhas2: #Verifica se as colunas e linhas são iguais (condição para poder multiplicar)
        raise ValueError("Numero de colunas da primeira matriz precisa ser igual ao numero de linhas da segunda")
    
    resultado= [[0]*colunas2 for _ in range(linhas1)] #O resultado terá a quantidade de linhas da matrizA e colunas da matrizB
    
    #Fazendo a multiplicação
    for i in range(linhas1): #Percorre as linhas da matrizA
        for j in range(colunas2): #Percorre as colunas da matrizB
            soma=0 
            for k in range(colunas1): #K serve como um carrinho que percorre os números da linha fixada na matrizA e da coluna fixada da matrizB
                soma += matriz1[i][k] * matriz2[k][j]
            resultado[i][j]=soma
    return resultado


for n in dimensoes:
    for j in dimensoes:
        for p in dimensoes:
            for q in dimensoes:
                if j == p: #Só vai funcionar se j==p
                    matrizA, matrizB= criar(n,j,p,q) #Atribuo as matrizes
                    tempoinicial= time.perf_counter() #Tempo mais preciso
                    mult(matrizA,matrizB) #Faz a multiplicação das duas
                    tempofinal= time.perf_counter() - tempoinicial
                    print(tempofinal) 
                    temposPy.append(tempofinal) #Coloca na lista de tempos da multiplicação feitos pelo python
                    matrizA=np.array(matrizA) #Transformo em array do numpy para conseguir usar as funções do próprio
                    matrizB=np.array(matrizB)
                    tempoinicial= time.perf_counter()
                    matrizA@matrizB #Multiplicação de matrizes pelo numpy
                    tempofinal= time.perf_counter() - tempoinicial
                    print(tempofinal) 
                    temposNP.append(tempofinal) #Coloco no tempo numpy
                    linhas_matriz_A.append(n) #Coloca na lista de linhas_matriz_A as linhas das matrizesA que já foram multiplicadas
                    colunas_matriz_B.append(q) #Mesma coisa so que com as colunas




#Ploto um gráfico 3D sendo o eixo x as linhas da matrizA e eixo y as colunas da matrizB e eixo z os tempos (Numpy ou Python)
linhas_matriz_A= np.array(linhas_matriz_A)
colunas_matriz_B= np.array(colunas_matriz_B)
temposPy= np.array(temposPy)
temposNP= np.array(temposNP)


fig = plt.figure(figsize=(14,8))
ax= fig.add_subplot(111, projection="3d")

temposPy_log= np.log10(temposPy)
temposNP_log= np.log10(temposNP)

ax.plot(linhas_matriz_A,colunas_matriz_B,temposPy_log, 'o-', c="red", label="Multiplicação Manual")
ax.plot(linhas_matriz_A,colunas_matriz_B,temposNP_log, 'o-', c="blue", label="Multiplicação Numpy")
ax.set_xlabel("Número de Linhas da Matriz A")
ax.set_ylabel("Número de Colunas da Matriz B")
ax.set_zlabel("Tempos (log10)")
ax.set_title("Comparação dos tempos de execução")
plt.legend()
plt.show()



