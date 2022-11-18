import numpy as np
import sympy as sp
import matplotlib as mp
import matplotlib.pyplot as plt
import os
os.stat("./")

# We obtain the data
times=[]
with open("times.txt","r", encoding='utf-8') as f:
    for line in f:
        times.append([float(x.strip()) for x in line.split(",")])

# We reduce the data to the same length
minum = len(times[0])
for i in times:
    if len(i) < minum:
        minum = len(i)-1

for i in range(len(times)):
    times[i] = times[i][:minum]

# We calculate the averages
averages = []
for i in range(minum):
    averages.append(sum([x[i] for x in times])/len(times))

# We show the graph
plt.title('Hilos vs tiempo', fontsize=22)
plt.grid()
plt.xticks([x+1 for x in range(minum)])

for i in times:
    plt.scatter([x+1 for x in range(minum)], [x*(10**-9) for x in i], s=5,zorder=2)
    plt.plot([x+1 for x in range(minum)],[x*(10**-9) for x in i], linewidth=1, zorder=1)
    
plt.scatter([x+1 for x in range(minum)], [x*(10**-9) for x in averages], s=100, c='b',zorder=4, marker="o")
plt.plot([x+1 for x in range(minum)],[x*(10**-9) for x in averages], linewidth=7, c='r',zorder=3,label="Average")

plt.legend()
plt.xlabel('Thread')
plt.ylabel('Time (s)')
plt.savefig("grafica.svg")
plt.show()
