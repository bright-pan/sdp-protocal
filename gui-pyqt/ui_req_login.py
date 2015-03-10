# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'req_login.ui'
#
# Created: Mon Mar 02 10:42:56 2015
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 218)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 180, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(60, 20, 281, 126))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.SequencelineEdit = QtGui.QLineEdit(self.widget)
        self.SequencelineEdit.setObjectName(_fromUtf8("SequencelineEdit"))
        self.gridLayout.addWidget(self.SequencelineEdit, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.IDlineEdit = QtGui.QLineEdit(self.widget)
        self.IDlineEdit.setObjectName(_fromUtf8("IDlineEdit"))
        self.gridLayout.addWidget(self.IDlineEdit, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.K0lineEdit = QtGui.QLineEdit(self.widget)
        self.K0lineEdit.setObjectName(_fromUtf8("K0lineEdit"))
        self.gridLayout.addWidget(self.K0lineEdit, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.VERSIONlineEdit = QtGui.QLineEdit(self.widget)
        self.VERSIONlineEdit.setObjectName(_fromUtf8("VERSIONlineEdit"))
        self.gridLayout.addWidget(self.VERSIONlineEdit, 3, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.K1lineEdit = QtGui.QLineEdit(self.widget)
        self.K1lineEdit.setObjectName(_fromUtf8("K1lineEdit"))
        self.gridLayout.addWidget(self.K1lineEdit, 4, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_5.setText(_translate("Dialog", "序号", None))
        self.label.setText(_translate("Dialog", "ID", None))
        self.label_2.setText(_translate("Dialog", "K0", None))
        self.label_3.setText(_translate("Dialog", "VERSION", None))
        self.label_4.setText(_translate("Dialog", "K1", None))

