import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

def semAnim(n):
    xs= [0]
    ys= [0]
    b= [0,1,2,3]
    for i in range(n):
        a= np.random.choice(b)
        if a==0:
            xs.append(xs[i]+1)
            ys.append(ys[i])
        elif a==1:
            xs.append(xs[i]-1)
            ys.append(ys[i])
        elif a==2:
            xs.append(xs[i])
            ys.append(ys[i]+1)
        elif a==3:
            xs.append(xs[i])
            ys.append(ys[i]-1)

    plt.plot(xs,ys)
    plt.show()

def animation(n):
    fig, ax= plt.subplots()
    line,= ax.plot([],[])

    xs= [0]
    ys= [0]
    b= [0,1,2,3]
    lines= []
    colors= ['r','g','b','y','m','c','orange','purple']
    i=0
    def update(frame, *fargs):  
        nonlocal i, colors
        if i < n:

            ax.set_xlim(min(xs)-1, max(xs)+1)
            ax.set_ylim(min(ys)-1, max(ys)+1)

            a= np.random.choice(b)
            if a==0:
                xs.append(xs[-1]+1)
                ys.append(ys[-1])
            elif a==1:
                xs.append(xs[-1]-1)
                ys.append(ys[-1])
            elif a==2:
                xs.append(xs[-1])
                ys.append(ys[-1]+1)
            elif a==3:
                xs.append(xs[-1])
                ys.append(ys[-1]-1)
            i+=1
            line, = ax.plot(xs[-2:], ys[-2:], color=colors[i % len(colors)], lw=2)
            lines.append(line)
            return lines,

    ani= FuncAnimation(fig, update, frames=n, interval=1000)
    plt.show()


animation(10)
semAnim(10000)