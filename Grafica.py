import numpy as np
import sympy as sp
import matplotlib as mp
import matplotlib.pyplot as plt
import matplotlib
# We obtain the data
times=[]
with open("times.txt","r", encoding='utf-8') as f:
    CPUname = f.readline().strip('\n')
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
plt.figure(figsize=(13,9))
fullScreen = plt.get_current_fig_manager()
fullScreen.resize(*fullScreen.window.maxsize())
plt.title(CPUname, fontsize=22)
plt.grid()
plt.xticks([x+1 for x in range(minum)])

plt.scatter([x+1 for x in range(minum)], [x*(10**-9) for x in averages], s=50, c="b", zorder=4, marker="o")
plt.plot([x+1 for x in range(minum)], [x*(10**-9) for x in averages], linewidth=5, c="r", zorder=3, label="Average")

for n, i in enumerate(times):
    plt.scatter([x+1 for x in range(minum)], [x*(10**-9) for x in i],s=5,zorder=2,marker="o")
    plt.plot([x+1 for x in range(minum)], [x*(10**-9) for x in i], linewidth=1, zorder=1, label="Test "+str(n+1))

    
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), shadow=True, fancybox=True)
plt.xlabel("Threads")
plt.ylabel("Time (s)")
plt.savefig(CPUname+".svg")
plt.show()
