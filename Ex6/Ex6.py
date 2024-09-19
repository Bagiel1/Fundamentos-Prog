import numpy as np
from matplotlib import pyplot as plt
import networkx as nx


class Ponto:
    def __init__(self,x,y):
        self.x= x
        self.y= y

xs=[]
ys=[]
linhas=[]

class Grafo:
    def __init__(self):
        self.matriz= []
        self.textos= []
        self.i=0

    def criarInicial(self,n):
        self.matriz= np.zeros(shape=(n,n), dtype=int)
        

    def mostrarGrafo(self):
        for i in self.matriz:
            print(i)
    
    
    def adicionarLigacao(self,n,z):
        self.matriz[n,z]= 1
        novacoordx= (xs[n],xs[z])
        novacoordy= (ys[n],ys[z])

        linha, = plt.plot(novacoordx,novacoordy,color='black',zorder=1)
        linhas.append((n,z,linha))
    
    def adicionarPonto(self,cx,cy):
        matriz_zero= np.zeros(shape=(len(self.matriz)+1,len(self.matriz)+1), dtype=int)
        matriz_zero[:len(self.matriz),:len(self.matriz)]= self.matriz
        self.matriz= matriz_zero
        ponto= Ponto(cx,cy)
        texto = plt.text(cx, cy + 0.2, str(self.i), fontsize=12, ha='center')
        self.textos.append(texto)
        xs.append(cx)
        ys.append(cy)
        self.i= self.i+1
    
    def plotarGrafico(self):
        
        self.grafico= plt.scatter(xs,ys,s=300,zorder=2)
        plt.show()

    def removerPonto(self,p):

        for (n, z, linha) in linhas[:]:  
            if n == p or z == p:
                linha.remove() 
                linhas.remove((n, z, linha))

        self.matriz= np.delete(self.matriz,p,axis=0)
        self.matriz= np.delete(self.matriz,p,axis=1)
        del xs[p]
        del ys[p]
        for texto in self.textos:
            texto.remove()
        self.textos.clear()
        for i,(x,y) in enumerate(zip(xs,ys)):
            texto= plt.text(x,y+0.2,str(i), fontsize=12, ha= 'center')
            self.textos.append(texto)
        

       

grafo= Grafo()
grafo.criarInicial(0)
grafo.adicionarPonto(0,0)
grafo.adicionarPonto(1,1)
grafo.adicionarPonto(2,1)
grafo.adicionarPonto(1,-1)
grafo.adicionarPonto(2,-1)
grafo.adicionarPonto(3.8,-1.2)
grafo.adicionarPonto(4,1.5)
grafo.adicionarPonto(5,0.3)
grafo.adicionarPonto(6,1.5)
grafo.adicionarPonto(6,-1)
grafo.adicionarLigacao(0,1)
grafo.adicionarLigacao(1,3)
grafo.adicionarLigacao(1,2)
grafo.adicionarLigacao(3,4)
grafo.adicionarLigacao(4,2)
grafo.adicionarLigacao(2,6)
grafo.adicionarLigacao(6,5)
grafo.adicionarLigacao(6,7)
grafo.adicionarLigacao(5,7)
grafo.adicionarLigacao(7,8)
grafo.adicionarLigacao(8,9)

grafo.mostrarGrafo()
grafo.plotarGrafico()





