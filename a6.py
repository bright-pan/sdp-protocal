# ! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Administrator'

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class MyQQ(QToolBox):
    def __init__(self, parent=None):
        super(MyQQ,self).__init__(parent)

        toolButton1_1=QToolButton()
        toolButton1_1.setText(self.tr("朽木"))
        toolButton1_1.setIcon(QIcon("image/koala.jpg"))
        toolButton1_1.setIconSize(QSize(60, 60))
        toolButton1_1.setAutoRaise(True)
        toolButton1_1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        toolButton1_2=QToolButton()
        toolButton1_2.setText(self.tr("朽木"))
        toolButton1_2.setIcon(QIcon("image/koala.jpg"))
        toolButton1_2.setIconSize(QSize(60, 60))
        toolButton1_2.setAutoRaise(True)
        toolButton1_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        toolButton2_1=QToolButton()
        toolButton2_1.setText(self.tr("朽木"))
        toolButton2_1.setIcon(QIcon("image/koala.jpg"))
        toolButton2_1.setIconSize(QSize(60, 60))
        toolButton2_1.setAutoRaise(True)
        toolButton2_1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        toolButton2_2=QToolButton()
        toolButton2_2.setText(self.tr("朽木"))
        toolButton2_2.setIcon(QIcon("image/koala.jpg"))
        toolButton2_2.setIconSize(QSize(60, 60))
        toolButton2_2.setAutoRaise(True)
        toolButton2_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        groupbox1 = QGroupBox()
        vlayout1=QVBoxLayout(groupbox1)
        vlayout1.setMargin(10)
        vlayout1.setAlignment(Qt.AlignCenter)
        #vlayout1.addStretch(20)
        vlayout1.addWidget(toolButton1_1)
        #vlayout1.addStretch(60)
        vlayout1.addWidget(toolButton1_2)
        vlayout1.addStretch()

        groupbox2 = QGroupBox()
        vlayout2=QVBoxLayout(groupbox2)
        vlayout2.setMargin(10)
        vlayout2.setAlignment(Qt.AlignCenter)
        vlayout2.addWidget(toolButton2_1)
        vlayout2.addWidget(toolButton2_2)
        vlayout2.addStretch()

        self.addItem(groupbox1, self.tr("我的家"))
        self.addItem(groupbox2, self.tr("我的家斯蒂芬"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myqq = MyQQ()
    myqq.show()
    sys.exit(app.exec_())

