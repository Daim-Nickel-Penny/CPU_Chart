import tkinter as tk
import  platform
import cpuinfo
import psutil
import matplotlib.pyplot as plt
import numpy as np
from tkinter.font import Font

cr1=(psutil.cpu_count())
cr2=(psutil.cpu_count(logical=False))
cpu=(psutil.cpu_count(logical=False))
name=psutil.users()[0].name
batper=psutil.sensors_battery().percent
plug=psutil.sensors_battery().power_plugged
discharge=psutil.sensors_battery().secsleft
load=psutil.getloadavg()
cpu_current=psutil.cpu_freq().current
cpu_max=psutil.cpu_freq().max
cpu_min=psutil.cpu_freq().min
host=psutil.users()[0].terminal
pid=psutil.users()[0].pid
bootTime=psutil.boot_time()
bsent=psutil.net_io_counters().bytes_sent;
brecv=psutil.net_io_counters().bytes_recv;
packsent=psutil.net_io_counters().packets_sent;
packrecv=psutil.net_io_counters().packets_recv;
dropin=psutil.net_io_counters().dropin;
dropout=psutil.net_io_counters().dropout;
diskDevice=psutil.disk_partitions()[0].device
mntPoint=psutil.disk_partitions()[0].mountpoint
fsType=psutil.disk_partitions()[0].fstype
diskdetail=psutil.disk_partitions()[0].opts
total=psutil.disk_usage('/').total
used=psutil.disk_usage('/').used
free=psutil.disk_usage('/').free
perct=psutil.disk_usage('/').percent

root = tk.Tk()
T = tk.Text(root, height=49, width=80)

T.pack()

T.insert(tk.END,"\t\t---------------------------------------------------\n")
T.insert(tk.END, f"\t\t█▓▒▒░░░ Welcome {name}. Your Processor's Data░░░▒▒▓█\n",)
T.insert(tk.END,"\t\t---------------------------------------------------\n")
T.insert(tk.END, " 𝑪𝑷𝑼 𝑫𝑬𝑻𝑨𝑰𝑳𝑺\n")
T.insert(tk.END, f" Number of Cores: {cr1}\n Physical Core:{cr2} \n\n")
T.insert(tk.END, " 𝑪𝑷𝑼 𝑭𝒓𝒆𝒒𝒖𝒆𝒏𝒄𝒚\n")
T.insert(tk.END, f" Current CPU Frequency in MHz {cpu_current}\n Maximum CPU Frequency in MHz {cpu_max}\n"
                 f" Minimum CPU Frequency in MHz {cpu_min}\n\n")
T.insert(tk.END, " 𝑩𝒂𝒕𝒕𝒆𝒓𝒚 𝑫𝒆𝒕𝒂𝒊𝒍𝒔\n")
T.insert(tk.END, f" Battery Percentage: {batper} \n Discharge Time Left: {discharge} \n Power Plugged: {plug}\n\n")
T.insert(tk.END, " 𝑼𝒔𝒆𝒓 𝑫𝒆𝒕𝒂𝒊𝒍𝒔\n")
T.insert(tk.END, f" Name:{name}\n Host: {host}\n PID of Login Process: {pid}\n")
T.insert(tk.END, f" Boot Time since the epoch: {bootTime}\n\n")
T.insert(tk.END, " 𝑵𝒆𝒕𝒘𝒐𝒓𝒌 𝑰𝒏𝒑𝒖𝒕 𝑶𝒖𝒕𝒑𝒖𝒕\n")
T.insert(tk.END, f" Bytes Sent: {bsent}\n Byte Recieved: {brecv} \n Packets Sent: {packsent} \n Packets Recieved: {packrecv}\n"
                 f" Incoming Packets Dropped: {dropin} \n Outgoing Packets Dropped: {dropout}\n\n")
T.insert(tk.END, " 𝑫𝒊𝒔𝒌 𝑷𝒂𝒓𝒕𝒊𝒕𝒊𝒐𝒏\n")
T.insert(tk.END, f" Device: {diskDevice}\n Mount Point: {mntPoint} \n File System Type: {fsType}\n Opt details: {diskdetail}\n\n")
T.insert(tk.END, " 𝑫𝒊𝒔𝒌 𝑺𝒕𝒐𝒓𝒂𝒈𝒆 𝑫𝒆𝒕𝒂𝒊𝒍𝒔\n")
T.insert(tk.END, f" Total Storage: {total}\n Used Space: {used}\n Free Space: {free} \n Percent: {perct}")
tk.mainloop()