from numpy import cbrt, power
import time

start = time.time()
for i in range(100000000):
    d = cbrt(123456789.123456789)
print(time.time()-start)

start = time.time()
for i in range(100000000):
    d = (123456789.123456789)**(1/3)
print(time.time()-start)

start = time.time()
for i in range(100000000):
    d = power(123456789.123456789,(1/3))
print(time.time()-start)
