import numpy as np
from matplotlib import pyplot as plt
import random


def verificacao(matriz,m,z):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i != 0 or j != 0) and matriz[m + i, z + j] == 1:
                return False
    return True
    


def programa():
    tamanho=400
    movimentos= [(1,0),(-1,0),(0,1),(0,-1)]
    matriz= np.zeros((tamanho+1,tamanho+1), dtype=int)
    matriz[tamanho//2,tamanho//2]= 1
    p=10

    for i in range(p):
        for j in range(p):
                
                i_inicial= np.random.randint(1,tamanho-1)
                j_inicial= np.random.randint(1,tamanho-1)

                if np.sqrt(i_inicial**2 + j_inicial**2) >= 180:
                    xs_t, ys_t= [i_inicial],[j_inicial]
                    c=0

                while xs_t[c] < tamanho and xs_t[c] > 0 and ys_t[c] < tamanho and ys_t[c] > 0:
                    if verificacao(matriz,xs_t[c],ys_t[c]): 

                        mx, my= random.choice(movimentos)
                        xs_t.append(xs_t[c]+mx)
                        ys_t.append(ys_t[c]+my)

                        c+=1
                    else:
                        matriz[xs_t[-1], ys_t[-1]] = 1
                        break

            


    fig, ax= plt.subplots()
    ax.imshow(matriz, cmap='binary', origin='lower')
    ax.set_xlim(0,tamanho)
    ax.set_ylim(0,tamanho)
    plt.show()


programa()