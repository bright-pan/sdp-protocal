# ! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Administrator'

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

import untitled

class MyDlg(QDialog, untitled.Ui_Dialog):
    def __init__(self, parent=None):
        super(MyDlg, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mydlg = MyDlg()
    mydlg.show()
    sys.exit(app.exec_())