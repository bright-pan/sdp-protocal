# ! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Administrator'

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class MyDlg(QWidget):
    def __init__(self, parent=None):
        super(MyDlg, self).__init__(parent)
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)

        self.lineedit.setFocus()
        self.lineedit.returnPressed.connect(self.updateUi)

    def updateUi(self):
        print self.lineedit.text()
        try:
            text = unicode(self.lineedit.text())
            self.browser.append("%s = <b>%s</b>" % (text, eval(text)))
        except ValueError:
            self.browser.append("<font color=red>%s is invalid!</font>" % text)
        #self.browser.setText(self.lineedit.text()+"\n")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = QDialog()
    my = MyDlg()
    my.show()
    sys.exit(app.exec_())