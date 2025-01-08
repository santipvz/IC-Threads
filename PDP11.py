from time import time_ns
from sys import argv
import miThread
from concurrent.futures import ProcessPoolExecutor

n = 16

if len(argv) > 1:
    n = int(argv[1])

hilos = []
# Quotient
c = 1000000 // n
# Module
r = 1000000 % n

with ProcessPoolExecutor() as executor:

    for i in range(n):
        # nr is the number of repetitions
        nr = c
        if r > 0:
            # nr varies accordind to the module of the division
            nr += 1
            r -= 1

        hilos.append(executor.submit(miThread.functionWithThread, nr))
        # print("Se ha creado el hilo", hilos[i].name)

    start = time_ns()

    for hilo in hilos:
        hilo.result()

# print("Todos los hilos han acabado")

end = time_ns()
print(f"{end-start}")
