import numpy as np
from matplotlib import pyplot as plt
import random

a= np.linspace(0,2*np.pi,1000)

f= (1+(1/2*(np.sin(a*2))**3))
g= (3+(1/2*(np.cos(a*3))**5))

xs=[]
ys=[]
xsf=[]
ysf=[]
pontos_dentro=0 
n=1000
for i in range(n):
    y= random.uniform(0,3.5)
    x= random.uniform(0,np.pi*2)
    index = int((x / (2*np.pi)) * len(a))
    if f[index] <= y <= g[index]:
        pontos_dentro+=1
        xs.append(x)
        ys.append(y)
    else:
        xsf.append(x)
        ysf.append(y)

valorArea= (pontos_dentro/n) * (2*np.pi*3.5)

print(valorArea)

plt.plot([a[0], a[0]], [f[0], g[0]], color= 'blue')
plt.plot([a[-1], a[-1]], [f[-1], g[-1]], color= 'blue')
plt.scatter(xs,ys,color='black', s=5)
plt.scatter(xsf,ysf,color='red', s=5)
plt.plot(a,f)
plt.plot(a,g)
plt.show()

