import numpy as np 
import random 
from matplotlib import pyplot as plt
from matplotlib import animation



def dados(M,N):
    resultados= []
    for i in range(N): #Quantidade de vezes jogadas
        b= (int(np.sum(np.random.randint(1,7, M)))) #Quantidade de dados jogados
        resultados.append(b)


    fig, (ax1,ax2)= plt.subplots(1,2)
    count, bins= np.histogram(resultados)    
    ax1.stairs(count, bins, fill=True, edgecolor='black')

    y= np.linspace(M, 6*M, 11)
    ax2.hist(resultados, bins=y, fill=True, edgecolor='black')
    
    

    plt.show()

dados(4,10000)







