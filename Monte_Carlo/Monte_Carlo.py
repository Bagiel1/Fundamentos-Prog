import numpy as np
from matplotlib import pyplot as plt
import random
from matplotlib.animation import FuncAnimation

def monte_carlo(N,pnts_por_frame):
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


print(monte_carlo(1000000,10000))