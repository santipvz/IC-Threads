import time
from threading import Thread
from numpy import tan
from numpy import arctan
from numpy import sqrt
import sys

n = 130

if len(sys.argv) > 1:
    n = int(sys.argv[1])

class miThread(Thread):
    
    def config(self, x):
        self.c1 = x

    def run(self):
        for i in range(self.c1):
            d = sqrt(tan(arctan(tan(arctan(tan(arctan(tan(arctan(tan(arctan(123456789.123456789)))))))))))
            #d = (123456789.123456789)**9.123456789


hilos = []
# Quotient
c = 1000000//n
# Module
r = 1000000%n    

for i in range(n):
    # nr is the number of repetitions
    nr = c
    if r > 0:
        # nr varies accordind to de module of the division
        nr+=1
        r-=1
    mT = miThread()
    mT.config(nr)
    hilos.append(mT)

start = time.time()

for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()

end = time.time()
print(f"{end-start}")

