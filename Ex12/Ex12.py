import numpy as np
from matplotlib import pyplot as plt
import random
a= np.linspace(0,2*np.pi,1000)
a_novo= np.linspace(0,3.5,1000)
a_= np.linspace(1,3.5)
f= (1+(1/2*(np.sin(a*2))**3))
g= (3+(1/2*(np.cos(a*3))**5))

h= 0.64*a_novo**2 - 2.88*a_novo + 2.24
j= -0.64*a_novo**2 + 2.88*a_novo + 2*np.pi-2.24

h_= 0.64*a_**2 - 2.88*a_ + 2.24
j_= -0.64*a_**2 + 2.88*a_ + 2*np.pi-2.24


xsf_g=[]
ysf_g=[]
xsf_f_g=[]
ysf_f_g=[]
pontos_dentro_f_g=0
n=100000

for i in range(n):
    y= random.uniform(0,3.5)
    x= random.uniform(0,np.pi*2)
    
    index = int((x / (2*np.pi)) * len(a))

    if f[index] <= y <= g[index]:
        pontos_dentro_f_g+=1
        xsf_g.append(x)
        ysf_g.append(y)
    else:
        xsf_f_g.append(x)
        ysf_f_g.append(y)
areaFG= (pontos_dentro_f_g/n)*(2*np.pi*3.5)

p=10000
pontos_dentro_h_j= 0
xsh_j=[]
ysh_j=[]
xsf_h_j= []
ysf_h_j= []
for i in range(p):

  y= random.uniform(0,3.5)
  x2= random.uniform(-1,0)
  x3= random.uniform(2*np.pi, 2*np.pi+1)
  index2= int((y/3.5)*len(a_novo))   
  if h[index2] < x2:
    pontos_dentro_h_j+=1
    xsh_j.append(x2)
    ysh_j.append(y)
  else:
      xsf_h_j.append(x2)
      ysf_h_j.append(y)

  if j[index2] > x3:
      pontos_dentro_h_j+=1
      xsh_j.append(x3)
      ysh_j.append(y)
  else:
     xsf_h_j.append(x3)
     ysf_h_j.append(y)
areaHJ= (pontos_dentro_h_j/p)*(3.5)

areatotal= areaFG+areaHJ
print(areatotal)


plt.scatter(xsf_g,ysf_g,color='black', s=5)
plt.scatter(xsf_f_g,ysf_f_g,color='white', s=5)
plt.scatter(xsh_j,ysh_j,color='black', s=5)
plt.scatter(xsf_h_j,ysf_h_j,color='white', s=5)
plt.plot(a,f)
plt.plot(a,g)
plt.plot(h_,a_)
plt.plot(j_,a_)

plt.show()