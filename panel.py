# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'panel.ui'
#
# Created: Fri Feb 26 11:43:30 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(360, 247)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.upButton = QtGui.QPushButton(self.centralwidget)
        self.upButton.setGeometry(QtCore.QRect(140, 50, 75, 41))
        self.upButton.setObjectName("upButton")
        self.downButton = QtGui.QPushButton(self.centralwidget)
        self.downButton.setGeometry(QtCore.QRect(140, 130, 75, 41))
        self.downButton.setObjectName("downButton")
        self.leftButton = QtGui.QPushButton(self.centralwidget)
        self.leftButton.setGeometry(QtCore.QRect(70, 90, 75, 41))
        self.leftButton.setObjectName("leftButton")
        self.rightButton = QtGui.QPushButton(self.centralwidget)
        self.rightButton.setGeometry(QtCore.QRect(210, 90, 75, 41))
        self.rightButton.setObjectName("rightButton")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        mainWindow.setTabOrder(self.upButton, self.rightButton)
        mainWindow.setTabOrder(self.rightButton, self.downButton)
        mainWindow.setTabOrder(self.downButton, self.leftButton)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.upButton.setText(QtGui.QApplication.translate("mainWindow", "Up", None, QtGui.QApplication.UnicodeUTF8))
        self.downButton.setText(QtGui.QApplication.translate("mainWindow", "Down", None, QtGui.QApplication.UnicodeUTF8))
        self.leftButton.setText(QtGui.QApplication.translate("mainWindow", "Left", None, QtGui.QApplication.UnicodeUTF8))
        self.rightButton.setText(QtGui.QApplication.translate("mainWindow", "Right", None, QtGui.QApplication.UnicodeUTF8))

