# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo_main.ui'
#
# Created: Fri Mar 06 16:14:01 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(809, 638)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(21, 1, 771, 581))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(self.widget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 2)
        self.epushButton = QtGui.QPushButton(self.widget)
        self.epushButton.setObjectName(_fromUtf8("epushButton"))
        self.gridLayout.addWidget(self.epushButton, 0, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.elineEdit = QtGui.QLineEdit(self.widget)
        self.elineEdit.setText(_fromUtf8(""))
        self.elineEdit.setObjectName(_fromUtf8("elineEdit"))
        self.gridLayout.addWidget(self.elineEdit, 1, 1, 1, 1)
        self.echeckBox_2 = QtGui.QCheckBox(self.widget)
        self.echeckBox_2.setObjectName(_fromUtf8("echeckBox_2"))
        self.gridLayout.addWidget(self.echeckBox_2, 1, 2, 1, 1)
        self.dpushButton = QtGui.QPushButton(self.widget)
        self.dpushButton.setObjectName(_fromUtf8("dpushButton"))
        self.gridLayout.addWidget(self.dpushButton, 1, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.textEdit = QtGui.QTextEdit(self.widget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 2, 1, 1, 3)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.textEdit_2 = QtGui.QTextEdit(self.widget)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.gridLayout.addWidget(self.textEdit_2, 3, 1, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "报文类型", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "登录报文", None))
        self.epushButton.setText(_translate("MainWindow", "编码", None))
        self.label_2.setText(_translate("MainWindow", "报文密钥", None))
        self.echeckBox_2.setText(_translate("MainWindow", "加解密", None))
        self.dpushButton.setText(_translate("MainWindow", "解码", None))
        self.label_3.setText(_translate("MainWindow", "明文区域", None))
        self.label_4.setText(_translate("MainWindow", "密文区域", None))

