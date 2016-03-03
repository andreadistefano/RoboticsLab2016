# -*- coding: utf-8 -*-

from ball import Ball
from time import sleep

b1 = Ball()
b1.start()

sleep(1)
b1.moveUp()
b1.moveUp()
b1.moveRight()
while True:
    sleep(0.5)