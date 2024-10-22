import numpy as np
from matplotlib import pyplot as plt
import random
import time



def montCarl3d(n):
    pontos_dentrox=[]
    pontos_dentroy=[]
    pontos_dentroz=[]
    pontos_forax=[]
    pontos_foray=[]
    pontos_foraz=[]
    total=0
    num=0
    start= time.time()
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
    end= time.time() - start
    print(f"Tempo normal= {end}")

    fig= plt.figure(figsize=(12,8))
    ax= fig.add_subplot(111,projection='3d')
    ax.scatter(pontos_dentrox,pontos_dentroy,pontos_dentroz, alpha=1, s=0.5)
    ax.scatter(pontos_forax,pontos_foray,pontos_foraz, color='r', alpha=0.3, s=0.2)
    plt.show()

    return pi_estimado


def montCarl3d_vet(n, externa=False):

    start= time.time()
    pontos= np.random.uniform(-1,1, (n,3))
    distancia= np.sum(pontos**2, axis=1)
    num= np.sum(distancia<=1)
    pi_estimado= 6*(num/n)
    end= time.time() - start
    print(f"Tempo Vetorizado= {end}")

    pontosdentro= pontos[distancia<=1]
    pontosfora= pontos[distancia>1]

    if externa == False:
        fig= plt.figure(figsize=(12,8))
        ax= fig.add_subplot(111, projection='3d')
        ax.scatter(pontosdentro[:,0],pontosdentro[:,1],pontosdentro[:,2], s=0.8)
        ax.scatter(pontosfora[:,0],pontosfora[:,1],pontosfora[:,2], alpha= 0.3, s=0.5)
        plt.show()  

    return pi_estimado


def monte_carloSemAni():
    num=0
    pis= []
    difmedias= []
    a= [10,10**2,10**3,10**4,10**5]
    for i in a:
        pis.append(montCarl3d_vet(i,externa=True))
    for p in pis:
        difmedias.append(abs(np.pi - p))

    print(f"# | {'N=10':>8} | {'N=10^2':>8} | {'N=10^3':>8} | {'N=10^4':>8} | {'N=10^5':>8}")
    print(f"  | {pis[0]:>8.5f} | {pis[1]:>8.5f} | {pis[2]:>8.5f} | {pis[3]:>8.5f} | {pis[4]:>8.5f}")

    plt.plot(a, difmedias, marker='o', linestyle='-', color='b')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('N')
    plt.ylabel('Diferença da média em relação a pi')
    plt.title('Diferença entre a média estimada de pi e o valor real de pi')
    plt.grid(True)
    plt.show()



print(montCarl3d(100000))
print(montCarl3d_vet(100000))
monte_carloSemAni()