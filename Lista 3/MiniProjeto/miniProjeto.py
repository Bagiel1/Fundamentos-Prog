import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt



def jacobi():
    N = 80
    L = 1
    Tensao = 2
    Lo = L / N
    massas = []
    pesos = []
    iniciais = []
    ysold = np.random.rand(N-1)
    g = 9.8

    iniciais = [0] * (N - 1)
    def aumentarExterna(i,New):
      iniciais[i] += New
    aumentarExterna(17,20)
    def rho(x):
        return 1

    for i in range(N-1):
        if i == 0:
            a = 0
            b = 3 * Lo / 2
        elif i == N - 2:
            a = L - 3 * Lo / 2
            b = L
        else:
            a = (i + 1) * Lo - Lo / 2
            b = (i + 1) * Lo + Lo / 2

        massa, _ = quad(rho, a, b)
        massas.append(massa)
        peso = -massa * g
        pesos.append(peso)

    tol = 1e-100
    maxit = 50000
    err = 10 * tol
    iter = 0

    while iter < maxit and err > tol:
        ynew = np.zeros(N-1)
        for i in range(N-1):
            yi_prev = ysold[i-1] if i > 0 else 0
            yi_next = ysold[i+1] if i < N-2 else 0
            ynew[i] = (yi_prev + yi_next)/2 - (massas[i]-iniciais[i])*Lo/2*Tensao

        err = np.linalg.norm(ynew - ysold)
        ysold = ynew.copy()
        iter += 1

    print("Deslocamentos:", ysold)

    plt.plot(ysold, marker='o')
    plt.title(f"Deslocamentos das Massas")
    plt.xlabel("Segmento")
    plt.ylabel("Deslocamento (y)")
    plt.grid(True)
    plt.show()





def jacobi2():

  N=80
  L= 1
  Tensao= 2
  Lo= L/N
  massas= []
  pesos= []
  iniciais=[]
  g= 9.8

  iniciais = [0] * (N - 1)
  def aumentarExterna(i,New):
    iniciais[i] += New
  

  def rho(x):
    return (1+np.exp(-100*(x-0.5)**2)/2)

  for i in range(N-1):
    if i == 0:
      a= 0
      b= 3*Lo/2
    elif i == N-2:
      a= L - 3*Lo/2
      b= L
    else:
      a= (i+1)*Lo-Lo/2
      b= (i+1)*Lo+Lo/2
    
    massa, er= quad(rho, a, b)
    massas.append(round(massa,2))
    peso= -massa * g
    pesos.append(round(peso,2))

  
  B= np.zeros((N-1, N-1))
  for i in range(N-1):
    B[i,i] = 2* Tensao / Lo
    
    if i > 0:
      B[i,i-1] = -Tensao / Lo
    
    if i < N-2:
      B[i, i+1] = -Tensao / Lo
  
  b= np.array(pesos) + iniciais

  O= np.diag(np.diag(B))
  L= np.tril(B, -1)
  U= np.triu(B, 1)

  yold= np.random.rand(N-1)

  tol= 1e-5
  maxit= 10000
  err= 10 * tol
  iter= 0
  
  while err > tol and iter < maxit:

    ynew= np.linalg.inv(O) @ (b - (L+U) @ yold)
    err= np.linalg.norm(ynew-yold)
    yold=ynew
    iter+=1

  print("Deslocamentos finais(y): ")
  print(yold)

  plt.plot(ynew, marker='o')
  plt.title(f"Deslocamentos das Massas")
  plt.xlabel("Segmento")
  plt.ylabel("Deslocamento (y)")
  plt.grid(True)
  plt.show()




def gauss_Seidel():

  N=80
  L= 1
  Tensao= 2
  Lo= L/N
  tensaoex= []
  massas= []
  pesos= []
  g= 9.8

  tensaoex= np.zeros(N-1)

  def aumentarExterna(i,New):
    tensaoex[i] += New

  def rho(x):
    return 1

  for i in range(N-1):
    if i == 0:
      a= 0
      b= 3*Lo/2
    elif i == N-2:
      a= L - 3*Lo/2
      b= L
    else:
      a= (i+1)*Lo-Lo/2
      b= (i+1)*Lo+Lo/2
    
    massa, er= quad(rho, a, b)
    massas.append(round(massa,2))
    peso= -massa * g
    pesos.append(round(peso,2))

  aumentarExterna(17,20)

  B= np.zeros((N-1, N-1))
  for i in range(N-1):
    B[i,i] = 2* Tensao / Lo
    
    if i > 0:
      B[i,i-1] = -Tensao / Lo
    
    if i < N-2:
      B[i, i+1] = -Tensao / Lo
  
  b= np.array(pesos) + tensaoex

  yold= np.random.rand(N-1)

  tol= 1e-5
  maxit= 100000
  iter= 0

  
  for k in range(maxit):
      ynew= yold.copy()

      for i in range(len(b)):
          alfa = np.dot(B[i, :i], ynew[:i]) + np.dot(B[i, i+1:], yold[i+1:])
          ynew[i] = (b[i] - alfa) / B[i, i]

      if np.linalg.norm(ynew - yold) < tol:
        print(ynew)
        plt.plot(ynew, marker='o')
        plt.title(f"Deslocamentos das Massas")
        plt.xlabel("Segmento")
        plt.ylabel("Deslocamento (y)")
        plt.grid(True)
        plt.show()
        return None
  
      yold= ynew
  


jacobi()
jacobi2()
gauss_Seidel()