# ! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Administrator'

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class MyTable(QTableWidget):
    def __init__(self,parent=None):
        super(MyTable,self).__init__(parent)

        self.setColumnCount(5)
        self.setRowCount(3)
        self.setItem(0,0,QTableWidgetItem(self.tr("姓名")))
        self.setItem(0,1,QTableWidgetItem(self.tr("性别")))
        self.setItem(0,2,QTableWidgetItem(self.tr("生日")))
        self.setItem(0,3,QTableWidgetItem(self.tr("职业")))
        self.setItem(0,4,QTableWidgetItem(self.tr("收入")))
        for i in range(1, 10):
            print i
            nameLabel = QLabel()
            nameLabel.setPixmap(QPixmap("image/koala.jpg"))
            self.setCellWidget(i,0,nameLabel)
            sexText = QTableWidgetItem(self.tr("男"))
            self.setItem(i,1, sexText)
            print "************"
            dte1=QDateTimeEdit()
            dte1.setDateTime(QDateTime.currentDateTime())
            dte1.setDisplayFormat("yyyy/mm/dd")
            dte1.setCalendarPopup(True)
            self.setCellWidget(i,2,dte1)
            cbw=QComboBox()
            cbw.addItem("Worker")
            cbw.addItem("Famer")
            cbw.addItem("Doctor")
            cbw.addItem("Lawyer")
            cbw.addItem("Soldier")
            self.setCellWidget(i,3,cbw)
            sb1=QSpinBox()
            sb1.setRange(1000,10000)
            self.setCellWidget(i,4,sb1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mytable = MyTable()
    mytable.show()
    sys.exit(app.exec_())