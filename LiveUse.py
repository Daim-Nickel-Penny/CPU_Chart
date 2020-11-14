import matplotlib.pyplot as plt
import matplotlib.animation as animation
import psutil
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(111)

cpu = []
def animate(i):
    cpu.append(psutil.cpu_percent())

    ax1.clear()
    ax1.plot(cpu)

ani = animation.FuncAnimation(fig, animate, interval = 1000)
plt.show()