# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'req_open.ui'
#
# Created: Mon Mar 02 17:08:13 2015
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
        Dialog.resize(381, 300)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(37, 37, 311, 171))
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
        self.TypeComboBox = QtGui.QComboBox(self.widget)
        self.TypeComboBox.setObjectName(_fromUtf8("TypeComboBox"))
        self.gridLayout.addWidget(self.TypeComboBox, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.AccountIDlineEdit = QtGui.QLineEdit(self.widget)
        self.AccountIDlineEdit.setObjectName(_fromUtf8("AccountIDlineEdit"))
        self.gridLayout.addWidget(self.AccountIDlineEdit, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.KeyIDlineEdit = QtGui.QLineEdit(self.widget)
        self.KeyIDlineEdit.setText(_fromUtf8(""))
        self.KeyIDlineEdit.setObjectName(_fromUtf8("KeyIDlineEdit"))
        self.gridLayout.addWidget(self.KeyIDlineEdit, 3, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.StatusComboBox = QtGui.QComboBox(self.widget)
        self.StatusComboBox.setObjectName(_fromUtf8("StatusComboBox"))
        self.gridLayout.addWidget(self.StatusComboBox, 4, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.OccurredTimelineEdit = QtGui.QLineEdit(self.widget)
        self.OccurredTimelineEdit.setObjectName(_fromUtf8("OccurredTimelineEdit"))
        self.gridLayout.addWidget(self.OccurredTimelineEdit, 5, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_5.setText(_translate("Dialog", "序号", None))
        self.label.setText(_translate("Dialog", "开门类型", None))
        self.label_2.setText(_translate("Dialog", "账户ID", None))
        self.label_4.setText(_translate("Dialog", "钥匙ID", None))
        self.label_6.setText(_translate("Dialog", "门锁状态", None))
        self.label_3.setText(_translate("Dialog", "发生时间", None))

