# ! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Administrator'

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys

class ZeroSpinBox(QSpinBox):
    zeros = 0
    def __init__(self, parent=None):
        super(ZeroSpinBox, self).__init__(parent)

        self.connect(self, SIGNAL("valueChanged(int)"), self.checkzero)
        self.connect(self, SIGNAL("atzero"), self.anounce)

    def anounce(self, zeros):
        print "ZeroSpinBox has been at zero %d times" % zeros

    def checkzero(self, value):
        print value
        if value == 0:
            self.zeros +=1
            self.emit(SIGNAL("atzero"), self.zeros)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    zerospinbox = ZeroSpinBox()
    zerospinbox.show()
    sys.exit(app.exec_())