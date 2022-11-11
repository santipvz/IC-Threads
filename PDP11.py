import time
from threading import Thread
from math import tan
from math import atan
import sys

n = 16

if len(sys.argv) > 1:
    n = int(sys.argv[1])

class miThread(Thread):
    def __init__(self, x):
        Thread.__init__(self)
        self.nr = x

    def run(self):
        for i in range(self.nr):
            d = (tan(atan(tan(atan(tan(atan(tan(atan(tan(atan(123456789.123456789)))))))))))**(1/3)
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
        # nr varies accordind to the module of the division
        nr+=1
        r-=1
    mT = miThread(nr)
    hilos.append(mT)

start = time.time()

for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()

end = time.time()
print(f"{end-start}")

