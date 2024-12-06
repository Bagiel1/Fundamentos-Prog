import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np


img= mpimg.imread('stinkbug.png')
A= img[:,:,0]
larg, comp, z= img.shape

img2= mpimg.imread('concrete.jpg')
C= img2[:,:,0]


def concreto(C,limiar):

    janela = C[100:250, 50:200]

    agregados= (janela < limiar) * 1

    fracao_agragados= np.sum(agregados) / agregados.size

    print(fracao_agragados)

    plt.imshow(agregados, cmap='gray')
    plt.show()
    

def suavizar(A, p=1, ativar=True):
    B= np.zeros_like(A, dtype=float)
    for i in range(larg):
        for j in range(comp):
            soma= A[i,j]
            contador=1

            if i > 0:
                soma += A[i-1, j]
                contador+=1
            if i < larg - 1:
                soma += A[i+1, j]
                contador+=1
            if j > 0:
                soma += A[i, j-1]
                contador+=1
            if j < comp - 1:
                soma += A[i, j+1]
                contador+=1

            B[i,j]= soma / contador
        
    if(ativar==True and p > 1):
        for i in range(p-1):
            B= suavizar(B, p=0, ativar=False)
    
    return B

def plotarSuave(A):
    plt.imshow(A)

def plotarPontos(n):

    colors= ['k'] * (n//2) + ['w'] * (n//2)
    np.random.shuffle(colors)
    coordsx= np.random.uniform(comp,size=n)
    coordsy= np.random.uniform(larg,size=n)
    plt.scatter(coordsx, coordsy, c=colors)
    plt.show()

def plotarNormal(A,n):
    
    if n == 1:
        plt.imshow(A)
    if n == 2:
        plt.imshow(A, cmap='hot')
    if n == 3:
        plt.imshow(A, cmap='nipy_spectral')
    plt.show()

def comparar(A):
    l= [1,2,3,5,10,15]
    exper=[]
    for i in l:
        a= float(suavizar(A, i)[0,0])
        exper.append(a)
    print(exper)



concreto(C, 120)



