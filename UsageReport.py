import psutil
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib.animation as animation
from collections import deque

print(psutil.sensors_battery())
fig = plt.figure()
ax = plt.axes(xlim=(0, 200), ylim=(0, 100))
line, = ax.plot([],[])

y_list = deque([-1]*400)
x_list = deque(np.linspace(200,0,num=400))


def init():
    line.set_data([],[])
    return line,


def animate(i):
    y_list.pop()
    y_list.appendleft(psutil.cpu_percent(None,False))
    line.set_data(x_list,y_list)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,frames=200, interval=100, blit=True)

plt.show()