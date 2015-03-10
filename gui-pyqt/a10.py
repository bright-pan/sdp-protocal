# ! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Administrator'

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_10_1
import ui_10_2
import ui_10_3

import sys

QTextCodec.setCodecForTr(QTextCodec.codecForName('utf8'))

from PyQt4 import uic

class TestDialog(QDialog):
    def __init__(self,parent=None):
        super(TestDialog,self).__init__(parent)
        firstUi=ui_10_1.Ui_Dialog()
        secondUi=ui_10_2.Ui_Dialog()
        self.thirdUi=ui_10_3.Ui_Dialog()
        tabWidget=QTabWidget(self)
        w1=QWidget()
        firstUi.setupUi(w1)
        w2=QWidget()
        secondUi.setupUi(w2)
        tabWidget.addTab(w1,"First")
        tabWidget.addTab(w2,"Second")
        tabWidget.resize(380,380)
        self.connect(firstUi.pushButton,SIGNAL("clicked() "),self.slotChild)
        self.connect(secondUi.pushButton,SIGNAL("clicked() "),self,SLOT("reject() "))
    def slotChild(self):
        dlg=QDialog()
        #self.thirdUi.setupUi(dlg)
        #a = uic.loadUi("ui_10_3.ui",dlg)
        dlg.exec_()
if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialog=TestDialog()
    dialog.show()
    sys.exit(app.exec_())