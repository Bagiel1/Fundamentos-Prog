import numpy as np
import matplotlib.pyplot as plt

p= np.linspace(0.5,1.2)

f = p
f_= (1/np.sqrt(p))

ys= [0.75]
xs=[0.75]
x=0.75

for i in range(1000):
    y= (1/np.sqrt(x))
    xs.append(float(x))
    xs.append(float(y))
    ys.append(float(y))
    ys.append(float(y))
    x=y

print(xs)
print(ys)

plt.plot(p, f)
plt.plot(p, f_)
plt.plot(xs, ys)
plt.show()