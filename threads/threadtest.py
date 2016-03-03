# -*- coding: utf-8 -*-

from threading import Thread
from time import sleep

class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self._counter = 0
        self._buffer = []

    def run(self):
        while 1:
            self._counter += 1
            self._buffer.append(self._counter)
            sleep(0.2)

    def getCounter(self):
        if (len(self._buffer) > 0):
            return self._buffer.pop(0)
        return self._counter

# Main

mt = MyThread()
mt.start()
counterMain = 100

while 1:
    print("counterMain:", counterMain)
    print ("Thread counter:", mt.getCounter())
    counterMain += 1
    sleep(0.5)