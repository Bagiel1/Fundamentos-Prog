import numpy as np
from matplotlib import pyplot as plt
import random
from numba import jit


def verificacao(matriz,m,z):
        if matriz[m,z+1] == 1 or matriz[m,z-1] == 1 or matriz[m+1,z-1] == 1 or matriz[m+1,z] == 1 or matriz[m+1,z+1] == 1 or matriz[m-1,z-1] == 1 or matriz[m-1,z] == 1 or matriz[m-1,z+1] == 1: 
            return False
        return True


def programa():
    q=399
    b= [0,1,2,3]
    xs= [q//2]
    ys= [q//2]
    matriz= np.zeros(shape=(q+1,q+1), dtype=int)
    matriz[q//2,q//2]= 1
    
    for i in range(1,q-1,3):
       
        for j in range(1,q-1,5):

            if np.sqrt(i**2 + j**2) >= q/2.2:
                xs_t= [i]
                ys_t= [j]
                c=0

                while xs_t[c] < q and xs_t[c] > 0 and ys_t[c] < q and ys_t[c] > 0:
                    if verificacao(matriz,xs_t[c],ys_t[c]): 

                        a= np.random.choice(b)
                        if a==0:
                            xs_t.append(xs_t[c]+1)
                            ys_t.append(ys_t[c])
                        elif a==1:
                            xs_t.append(xs_t[c]-1)
                            ys_t.append(ys_t[c])
                        elif a==2:
                            xs_t.append(xs_t[c])
                            ys_t.append(ys_t[c]+1)
                        elif a==3:
                            xs_t.append(xs_t[c])
                            ys_t.append(ys_t[c]-1)
                        c+=1
                    
                    else:
    
                        xs.append(xs_t[-1])
                        ys.append(ys_t[-1])
                        matriz[xs_t[-1], ys_t[-1]] = 1
                        break

            


    fig, ax= plt.subplots()
    ax.scatter(xs,ys)
    ax.set_xlim(0,q)
    ax.set_ylim(0,q)
    plt.show()


programa()