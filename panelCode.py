# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from visual import *
from ball import Ball
from panel import Ui_mainWindow


class MyPanel(Ui_mainWindow):
    def __init__(self):
        self._ball = Ball()

    def setupUi(self, mainWindow):
        super(MyPanel, self).setupUi(mainWindow)
        self.connectGUI()

    def connectGUI(self):
        self.upButton.clicked.connect(self.goUp)
        self.downButton.clicked.connect(self.goDown)
        self.leftButton.clicked.connect(self.goLeft)
        self.rightButton.clicked.connect(self.goRight)

    def goUp(self):
        print("Go up")
        self._ball.moveUp();

    def goDown(self):
        print("Go down")
        self._ball.moveDown();

    def goLeft(self):
        print("Go left")
        self._ball.moveLeft();

    def goRight(self):
        print("Go right")
        self._ball.moveRight();