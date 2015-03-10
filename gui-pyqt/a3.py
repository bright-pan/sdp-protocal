#coding=utf-8

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MyDlg(QDialog):
    def __init__(self, parent=None):
        super(MyDlg,self).__init__(parent)
        x_label = QLabel("X:")
        y_label = QLabel("Y:")
        xc_label = QLabel()
        yc_label = QLabel()

        layout = QGridLayout()
        layout.addWidget(x_label, 0, 0)
        layout.addWidget(xc_label, 0, 1)
        layout.addWidget(y_label, 1, 0)
        layout.addWidget(yc_label, 1, 1)
        self.setLayout(layout)
        temp = QString()
        xc_label.setText(temp.setNum(self.geometry().x()))
        yc_label.setText(temp.setNum(self.y()))
        print self.frameGeometry(), self.x(), self.y(), self.rect(), self.size(), self.geometry(), self.pos()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    md = MyDlg()
    md.show()
    sys.exit(app.exec_())