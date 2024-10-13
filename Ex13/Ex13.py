import numpy as np
from matplotlib import pyplot as plt
import random



def montCarl3d(n):
    pontos_dentrox=[]
    pontos_dentroy=[]
    pontos_dentroz=[]
    pontos_forax=[]
    pontos_foray=[]
    pontos_foraz=[]
    total=0
    num=0
    for i in range(n):
        x= random.uniform(-1,1)
        y= random.uniform(-1,1)
        z= random.uniform(-1,1)
        total+=1

        if x**2 + y**2 + z**2 <= 1:
            pontos_dentrox.append(x)
            pontos_dentroy.append(y)
            pontos_dentroz.append(z)
            num+=1
        else:
            pontos_forax.append(x)
            pontos_foray.append(y)
            pontos_foraz.append(z)

    pi_estimado= 6*(num/total)

    fig= plt.figure(figsize=(12,8))
    ax= fig.add_subplot(111,projection='3d')
    ax.scatter(pontos_dentrox,pontos_dentroy,pontos_dentroz, alpha=1, s=0.5)
    ax.scatter(pontos_forax,pontos_foray,pontos_foraz, color='r', alpha=0.3, s=0.2)
    plt.show()

    return pi_estimado


def montCarl3d_vet(n):

    pontos= np.random.uniform(-1,1, (n,3))
    distancia= np.sum(pontos**2, axis=1)
    num= np.sum(distancia<=1)
    pi_estimado= 6*(num/n)

    pontosdentro= pontos[distancia<=1]
    pontosfora= pontos[distancia>1]

    fig= plt.figure(figsize=(12,8))
    ax= fig.add_subplot(111, projection='3d')
    ax.scatter(pontosdentro[:,0],pontosdentro[:,1],pontosdentro[:,2], s=0.8)
    ax.scatter(pontosfora[:,0],pontosfora[:,1],pontosfora[:,2], alpha= 0.3, s=0.5)
    plt.show()

    return pi_estimado

pi= montCarl3d_vet(10000000)
print(pi)




