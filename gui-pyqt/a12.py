# ! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Administrator'
import sys
from PyQt4 import QtGui, QtCore
class Communicate(QtCore.QObject):
    closeApp = QtCore.pyqtSignal()
    print "A"
class Example(QtGui.QMainWindow, Communicate):

    def __init__(self):
        super(Example, self).__init__()
        print "B"
        self.initUI()
    def initUI(self):
        #self.c = Communicate()
        self.closeApp.connect(self.close)
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()
    def mousePressEvent(self, event):
        self.closeApp.emit()
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()