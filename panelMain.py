# -*- coding: utf-8 -*-

from PySide import QtGui
import sys
import panelCode


def startApp():
    app = QtGui.QApplication(sys.argv)
    wndMainWindow = QtGui.QMainWindow()
    ui = panelCode.MyPanel()
    ui.setupUi(wndMainWindow)
    wndMainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    startApp()
