import  platform
import cpuinfo
import psutil
import matplotlib.pyplot as plt
import numpy as np
import tkinter
from tkinter import messagebox


# print(platform.processor())
print(cpuinfo.get_cpu_info())
print(psutil.cpu_freq(percpu=True))

print(psutil.cpu_count(logical=False))




# while True:
#     cpu=(psutil.cpu_percent(interval=1))
#     print(cpu)
#
#     if cpu>50:
#        print("Upper Limit")
#        break
