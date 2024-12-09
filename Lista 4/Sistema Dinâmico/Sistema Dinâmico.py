import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib.animation import FuncAnimation



def iniciarEq(massa1,massa2,caminho):

    def forca(gamma, r1, r2):
        r12= r1 - r2
        dist= np.linalg.norm(r12)
        if dist < 1e-5:  
            dist = 1e-5
        return (-gamma*massa1*massa2*r12)/((np.linalg.norm(r12))**3)


    n=0
    tfin= 10
    dt= 0.001
    gamma= 1
    t= [0]

    r1 = [np.array([0.0, 0.0])]
    r2 = [np.array([1.0, 0.0])]

    v1 = [np.array([0.0, 0.0])]
    v2 = [np.array([0.0, 1.0])]

    forc= forca(gamma, r1[0], r2[0])

    a1= [forc/massa1]
    a2= [-forc/massa2]


    with open(caminho, 'w+') as evolfile:

        while t[n] < tfin:

            r1dps= r1[n] + v1[n]*dt + 0.5*a1[n]*dt**2
            r2dps= r2[n] + v2[n]*dt + 0.5*a2[n]*dt**2

            forc2= forca(gamma,r1dps,r2dps)
            
            a1dps= forc2/massa1
            a2dps= -forc2/massa2

            v1dps= v1[n] + 0.5*(a1[n]+a1dps)*dt
            v2dps= v2[n] + 0.5*(a2[n]+a2dps)*dt

            t.append(t[n]+dt)
            r1.append(r1dps)
            r2.append(r2dps)
            v1.append(v1dps)
            v2.append(v2dps)
            a1.append(a1dps)
            a2.append(a2dps)

            evolfile.write(f"{t[n]:.5f} {r1dps[0]:.5f} {r1dps[1]:.5f} {v1dps[0]:.5f} {v1dps[1]:.5f} "
            f"{r2dps[0]:.5f} {r2dps[1]:.5f} {v2dps[0]:.5f} {v2dps[1]:.5f}\n")

            n+=1

    r1= np.array(r1)
    r2= np.array(r2)

    return caminho


def carregarDados(arquivo, massa1, massa2):

    dados= np.loadtxt(arquivo)

    t= dados[:,0]
    r1x, r1y = dados[:, 1], dados[:, 2] 
    v1x, v1y = dados[:, 3], dados[:, 4] 
    r2x, r2y = dados[:, 5], dados[:, 6]  
    v2x, v2y = dados[:, 7], dados[:, 8]  

    K = 0.5 * massa1 * (v1x**2 + v1y**2) + 0.5 * massa2 * (v2x**2 + v2y**2)
    

    fig, (ax1,ax2) = plt.subplots(1, 2, figsize=(15, 6))

    ax1.plot(r1x, r1y, label='Corpo 1 (Trajetória)', color='b')
    ax1.plot(r2x, r2y, label='Corpo 2 (Trajetória)', color='r')
    ax1.scatter(r1x[0], r1y[0], color='b', label='Posição inicial Corpo 1')
    ax1.scatter(r2x[0], r2y[0], color='r', label='Posição inicial Corpo 2')
    ax1.set_xlabel('Posição X')
    ax1.set_ylabel('Posição Y')
    ax1.set_title('Trajetórias dos Corpos')
    ax1.legend()
    ax1.grid(True)

    ax2.plot(t, K, label='Energia Cinética Total', color='g')
    ax2.set_xlabel('Tempo (t)')
    ax2.set_ylabel('Energia Cinética Total (K)')
    ax2.set_title('Energia Cinética Total como função do tempo')
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout()
    plt.show()



def animarMovi(arquivo, massa1, massa2):
    dados= np.loadtxt(arquivo)

    t= dados[:,0]
    r1x, r1y = dados[:, 1], dados[:, 2] 
    r2x, r2y = dados[:, 5], dados[:, 6]  

    fig, ax= plt.subplots(figsize= (8,8))
    ax.set_xlabel("Posição X")
    ax.set_ylabel("Posição Y")
    ax.set_title("Animação do Movimento dos Corpos")
    ax.grid(True)

    corpo1, = ax.plot([],[], 'bo', label='Corpo 1', markersize=8)
    corpo2, = ax.plot([], [], 'ro', label='Corpo 2', markersize=8)
    traj1, = ax.plot([], [], 'b-', lw=1, alpha=0.6)
    traj2, = ax.plot([], [], 'r-', lw=1, alpha=0.6)
    ax.legend()

    def init():
        corpo1.set_data([],[])
        corpo2.set_data([],[])
        traj1.set_data([],[])
        traj2.set_data([],[])
        return corpo1, corpo2, traj1, traj2
    
    def update(frame):
        
        corpo1.set_data([r1x[frame]], [r1y[frame]])
        corpo2.set_data([r2x[frame]], [r2y[frame]])
        traj1.set_data(r1x[:frame+1], r1y[:frame+1])
        traj2.set_data(r2x[:frame+1], r2y[:frame+1])

        xmin = min(r1x[:frame+1].min(), r2x[:frame+1].min())
        xmax = max(r1x[:frame+1].max(), r2x[:frame+1].max())
        ymin = min(r1y[:frame+1].min(), r2y[:frame+1].min())
        ymax = max(r1y[:frame+1].max(), r2y[:frame+1].max())
        margin = 0.1 * max(xmax - xmin, ymax - ymin) 
        ax.set_xlim(xmin - margin, xmax + margin)
        ax.set_ylim(ymin - margin, ymax + margin)

        return corpo1, corpo2, traj1, traj2
    
    anim= FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=0.01)

    plt.show()


massa1, massa2= 1,1
animarMovi(iniciarEq(massa1,massa2,'C:/Users/Gabri/Desktop/Gabriel/Programação/Pyton/FDP/Lista 4/Sistema Dinâmico/evol.txt'), massa1, massa2)
