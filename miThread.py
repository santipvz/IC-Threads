from threading import Thread
from math import tan
from math import atan

class miThread(Thread):
    def __init__(self, x):
        Thread.__init__(self)
        self.nr = x

    def run(self):
        for i in range(self.nr):
            d = (tan(atan(tan(atan(tan(atan(tan(atan(tan(atan(123456789.123456789)))))))))))**(1/3)
