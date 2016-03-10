# -*- coding: utf-8 -*-

from panel import Ui_mainWindow
from time import sleep
import socket

class MyPanel(Ui_mainWindow):
    def __init__(self):
        self._sockMainServer = None
        self._mySocket = None
        self._myWindow = None
        sleep(0.5)

    def setupUi(self, mainWindow):
        super(MyPanel, self).setupUi(mainWindow)
        self._myWindow = mainWindow
        self.connectUI()

    def connectServer(self):
        self._sockMainServer = s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sockMainServer.connect(("localhost", 25000))
        self._sockMainServer.sendall("Hello world")
        data = s.recv(1024)
        print "Received:", data
        newPort = int(data)
        self._sockMainServer.close()
        sleep(0.25)
        self._mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._mySocket.connect(("localhost", newPort))

    def connectUI(self):
        self.upButton.clicked.connect(self.goUp)
        self.downButton.clicked.connect(self.goDown)
        self.leftButton.clicked.connect(self.goLeft)
        self.rightButton.clicked.connect(self.goRight)
        self.connectServer()

    def goUp(self):
        self._mySocket.sendall("Up")
        print("Go up")
        data = self._mySocket.recv(1024)
        print data

    def goDown(self):
        self._mySocket.sendall("Down")
        print("Go down")
        data = self._mySocket.recv(1024)
        print data

    def goLeft(self):
        self._mySocket.sendall("Left")
        print("Go left")
        data = self._mySocket.recv(1024)
        print data

    def goRight(self):
        self._mySocket.sendall("Right")
        print("Go right")
        data = self._mySocket.recv(1024)
        print data

    def closeEvent(self, event):
        pass
