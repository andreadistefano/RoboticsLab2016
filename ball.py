# -*- coding: utf-8 -*-

from visual import *


class Ball:
    def __init__(self):
        self._deltat = 0.005
        self._t = 0
        self._ball = sphere(pos=(0, 2, 0), radius=2, color=color.red)
        self._floor = box(pos=(0, 0, 0), size=(10, 0.1, 10), color=color.blue)

    def moveUp(self):
        self._ball.velocity = vector(0, 0, -1)
        self._ball.pos += self._ball.velocity * self._deltat

    def moveDown(self):
        self._ball.velocity = vector(0, 0, 1)
        self._ball.pos += self._ball.velocity * self._deltat

    def moveLeft(self):
        self._ball.velocity = vector(-1, 0, 0)
        self._ball.pos += self._ball.velocity * self._deltat

    def moveRight(self):
        self._ball.velocity = vector(1, 0, 0)
        self._ball.pos += self._ball.velocity * self._deltat
