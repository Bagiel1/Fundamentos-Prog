import numpy as np
import matplotlib.pyplot as plt

def forca(massa1,massa2, gamma, r1, r2):
    r12= r2 - r1
    return -((gamma*massa1*massa2)*(r12))/(np.linalg.norm(r12)**3)


n=0
tfin= 100
dt= 0.001
massa1,massa2,gamma= 1,1,1
t=[0]

r1 = [np.array([0.0, 0.0])]
r2 = [np.array([1.0, 0.0])]

v1 = [np.array([0.0, 0.0])]
v2 = [np.array([0.0, 1.0])]

a1= [forca(massa1, massa2, gamma, r1[0], r2[0])/massa1]
a2= [forca(massa2,massa1,gamma,r2[0],r1[0])/massa2]

evolfile= open('evol.txt', 'w+')

while t[n] < tfin:

    r1dps= r1[n] + v1[n]*dt + 0.5*a1[n]*dt**2
    r2dps= r2[n] + v2[n]*dt + 0.5*a2[n]*dt**2
    
    a1dps= forca(massa1,massa2,gamma,r1dps,r2dps)/massa1
    a2dps= forca(massa2,massa1,gamma,r2dps,r1dps)/massa2

    v1dps= v1[n] + 0.5*(a1[n]+a1dps)*dt
    v2dps= v2[n] + 0.5*(a2[n]+a2dps)*dt

    t.append(t[n] + dt)
    r1.append(r1dps)
    r2.append(r2dps)
    v1.append(v1dps)
    v2.append(v2dps)
    a1.append(a1dps)
    a2.append(a2dps)

    evolfile.write(f"{t[n]:.5f} {r1dps[0]:.5f} {r1dps[1]:.5f} {v1dps[0]:.5f} {v1dps[1]:.5f} "
    f"{r2dps[0]:.5f} {r2dps[1]:.5f} {v2dps[0]:.5f} {v2dps[1]:.5f}\n")

    n+=1

evolfile.close()

r1= np.array(r1)
r2= np.array(r2)

plt.plot(r1[:,0], r1[:,1], label='Corpo 1', color='b')
plt.plot(r2[:,0], r2[:,1], label='Corpo 2', color='r')
plt.scatter(r1[0,0], r1[0,1], color='b')
plt.scatter(r2[0,0], r2[0,1], color='r')
plt.legend()
plt.grid()
plt.show()
