import numpy as np
from matplotlib import pyplot as plt
import random
from matplotlib.animation import FuncAnimation
from numba import jit

def monte_carloAni(N,pnts_por_frame):
    pontos_dentroX=[]
    pontos_foraX=[]
    pontos_dentroY=[]
    pontos_foraY=[]
    
    fig, (axis,axis2)= plt.subplots(2,1, figsize=(16,8))

    axis.set_xlim(-1, 1)
    axis.set_ylim(-1, 1)    
    axis2.set_ylim(-1, 3.5)
    axis2.axhline(y=np.pi, color='g', linestyle='--', label='π (3.14)')
    axis2.axhline(y=0, color='g', linestyle='--', label='0')
    axis2.legend()
    axis.set_aspect('equal')

    plot_dentro,= axis.plot([],[], 'bo', markersize='2')
    plot_fora,= axis.plot([],[], 'ro', markersize='2')
    dif,= axis2.plot([],[])
    diferenca,= axis2.plot([],[])

    num= 0
    total= 0
    
    b=[]
    c=[]
    def update(frame, *fargs):
        nonlocal num, total, b, c
        
        if total <= N:
            for i in range(pnts_por_frame):
                x= random.uniform(-1,1)
                y= random.uniform(-1,1)

                total+=1

                if x**2 + y**2 <= 1:
                    pontos_dentroX.append(x)
                    pontos_dentroY.append(y)
                    num+=1
                else:
                    pontos_foraX.append(x)
                    pontos_foraY.append(y)

                pi_estimado = 4 * (num / total)
                dife= (np.pi - pi_estimado)
                c.append(dife)
                b.append(pi_estimado)
        
            diferenca.set_data(range(len(b)), b)
            dif.set_data(range(len(b)), c)
            plot_dentro.set_data(pontos_dentroX, pontos_dentroY)
            plot_fora.set_data(pontos_foraX,pontos_foraY)

            axis2.set_xlim(0, len(b))
        
        

        return plot_dentro, plot_fora, diferenca, dif
    
    animation= FuncAnimation(fig, update, frames=10, interval=10)
    plt.show()

    return 4 * (num / total)




def monte_carloSemAni():
    num=0
    pis= []
    a= [10**3,10**4,10**5,10**6,10**7]
    for j in a:
        total=j
        for l in range(4):
            num=0
            for i in range(j):
                x= random.uniform(-1,1)
                y= random.uniform(-1,1)
                if x**2 + y**2 <= 1:
                    num+=1
            pi_estimado= 4 * (num/total)
            pis.append(float(pi_estimado))
    
    medias_por_n = [(sum(pis[i:i+4])/4) for i in range(0,len(pis),4)] 
    print(medias_por_n) 
    difmedias = [abs(np.pi - media) for media in medias_por_n]

    print(f"# | {'N=10^3':>8} | {'N=10^4':>8} | {'N=10^5':>8} | {'N=10^6':>8} | {'N=10^7':>8}")
    print(f"1 | {pis[0]:>8.5f} | {pis[4]:>8.5f} | {pis[8]:>8.5f} | {pis[12]:>8.5f} | {pis[16]:>8.5f}")
    print(f"2 | {pis[1]:>8.5f} | {pis[5]:>8.5f} | {pis[9]:>8.5f} | {pis[13]:>8.5f} | {pis[17]:>8.5f}")
    print(f"3 | {pis[2]:>8.5f} | {pis[6]:>8.5f} | {pis[10]:>8.5f} | {pis[14]:>8.5f} | {pis[18]:>8.5f}")
    print(f"4 | {pis[3]:>8.5f} | {pis[7]:>8.5f} | {pis[11]:>8.5f} | {pis[15]:>8.5f} | {pis[19]:>8.5f}")

    plt.plot(a, difmedias, marker='o', linestyle='-', color='b')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('N')
    plt.ylabel('Diferença da média em relação a pi')
    plt.title('Diferença entre a média estimada de pi e o valor real de pi')
    plt.grid(True)
    plt.show()

monte_carloSemAni()
            