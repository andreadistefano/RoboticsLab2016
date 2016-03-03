# -*- coding: utf-8 -*-

from ball import Ball
from panel import Ui_mainWindow
from time import sleep


class MyPanel(Ui_mainWindow):
    def __init__(self):
        self._ball = Ball()
        sleep(0.5)
        self._ball.start()

    def setupUi(self, mainWindow):
        super(MyPanel, self).setupUi(mainWindow)
        self._myWindow = mainWindow
        self.connectGUI()

    def connectGUI(self):
        self.upButton.clicked.connect(self.goUp)
        self.downButton.clicked.connect(self.goDown)
        self.leftButton.clicked.connect(self.goLeft)
        self.rightButton.clicked.connect(self.goRight)

    def goUp(self):
        print("Go up")
        self._ball.moveUp()

    def goDown(self):
        print("Go down")
        self._ball.moveDown()

    def goLeft(self):
        print("Go left")
        self._ball.moveLeft()

    def goRight(self):
        print("Go right")
        self._ball.moveRight();

    def closeEvent(self, event):
        self._ball.close()
        self._ball.join()
        self._ball = None