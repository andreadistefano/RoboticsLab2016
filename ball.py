# -*- coding: utf-8 -*-

import visual
from threading import Thread
from time import sleep


class Ball(Thread):
    def __init__(self):
        Thread.__init__(self)
        self._ball = visual.sphere(pos=(0, 0.5, 0), radius=0.5, color=visual.color.red)
        self._floor = visual.box(pos=(0, 0, 0), size=(10, 0.1, 10), color=visual.color.blue)
        self._action = ""
        self._actionBuf = []

    def run(self):
        while True:
            visual.rate(30)
            if len(self._actionBuf) > 0:
                self._action = self._actionBuf.pop(0)
                if self._action == "U":
                    step = visual.vector(0, 0, -1)
                    self._ball.pos += step
                    self._action = ""
                elif self._action == "D":
                    step = visual.vector(0, 0, 1)
                    self._ball.pos += step
                    self._action = ""
                elif self._action == "L":
                    step = visual.vector(-1, 0, 0)
                    self._ball.pos += step
                    self._action = ""
                elif self._action == "R":
                    step = visual.vector(1, 0, 0)
                    self._ball.pos += step
                    self._action = ""
                elif self._action == "0":
                    exit()
                    break
            sleep(0.2)

    def moveUp(self):
        self._actionBuf.append("U")

    def moveDown(self):
        self._actionBuf.append("D")

    def moveLeft(self):
        self._actionBuf.append("L")

    def moveRight(self):
        self._actionBuf.append("R")

    def close(self):
        self._actionBuf.append("0")

    def command(self, msg):
        pass