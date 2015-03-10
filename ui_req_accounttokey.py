# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'req_accounttokey.ui'
#
# Created: Thu Mar 05 10:11:05 2015
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
        Dialog.resize(404, 339)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 290, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(41, 32, 321, 161))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.SequencelineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.SequencelineEdit.setObjectName(_fromUtf8("SequencelineEdit"))
        self.gridLayout.addWidget(self.SequencelineEdit, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.AccountIDlineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.AccountIDlineEdit.setObjectName(_fromUtf8("AccountIDlineEdit"))
        self.gridLayout.addWidget(self.AccountIDlineEdit, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.KeyIDlineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.KeyIDlineEdit.setText(_fromUtf8(""))
        self.KeyIDlineEdit.setObjectName(_fromUtf8("KeyIDlineEdit"))
        self.gridLayout.addWidget(self.KeyIDlineEdit, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.OccurredTimelineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.OccurredTimelineEdit.setObjectName(_fromUtf8("OccurredTimelineEdit"))
        self.gridLayout.addWidget(self.OccurredTimelineEdit, 3, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_5.setText(_translate("Dialog", "序号", None))
        self.label_2.setText(_translate("Dialog", "账户ID", None))
        self.label_4.setText(_translate("Dialog", "钥匙ID", None))
        self.label_3.setText(_translate("Dialog", "发生时间", None))

