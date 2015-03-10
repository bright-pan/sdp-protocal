# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'req_keymodify.ui'
#
# Created: Thu Mar 05 15:10:41 2015
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
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(40, 31, 321, 230))
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
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.KeyTypeComboBox = QtGui.QComboBox(self.widget)
        self.KeyTypeComboBox.setObjectName(_fromUtf8("KeyTypeComboBox"))
        self.gridLayout.addWidget(self.KeyTypeComboBox, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.AuthTypeComboBox = QtGui.QComboBox(self.widget)
        self.AuthTypeComboBox.setObjectName(_fromUtf8("AuthTypeComboBox"))
        self.gridLayout.addWidget(self.AuthTypeComboBox, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.KeyIDlineEdit = QtGui.QLineEdit(self.widget)
        self.KeyIDlineEdit.setObjectName(_fromUtf8("KeyIDlineEdit"))
        self.gridLayout.addWidget(self.KeyIDlineEdit, 3, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.KeyCodelineEdit = QtGui.QLineEdit(self.widget)
        self.KeyCodelineEdit.setText(_fromUtf8(""))
        self.KeyCodelineEdit.setObjectName(_fromUtf8("KeyCodelineEdit"))
        self.gridLayout.addWidget(self.KeyCodelineEdit, 4, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.widget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.StartTimelineEdit = QtGui.QLineEdit(self.widget)
        self.StartTimelineEdit.setObjectName(_fromUtf8("StartTimelineEdit"))
        self.gridLayout.addWidget(self.StartTimelineEdit, 5, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.widget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)
        self.EndTimelineEdit = QtGui.QLineEdit(self.widget)
        self.EndTimelineEdit.setObjectName(_fromUtf8("EndTimelineEdit"))
        self.gridLayout.addWidget(self.EndTimelineEdit, 6, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)
        self.WeeklylineEdit = QtGui.QLineEdit(self.widget)
        self.WeeklylineEdit.setObjectName(_fromUtf8("WeeklylineEdit"))
        self.gridLayout.addWidget(self.WeeklylineEdit, 7, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 8, 0, 1, 1)
        self.OccurredTimelineEdit = QtGui.QLineEdit(self.widget)
        self.OccurredTimelineEdit.setObjectName(_fromUtf8("OccurredTimelineEdit"))
        self.gridLayout.addWidget(self.OccurredTimelineEdit, 8, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_5.setText(_translate("Dialog", "序号", None))
        self.label_6.setText(_translate("Dialog", "权限类型", None))
        self.label.setText(_translate("Dialog", "钥匙类型", None))
        self.label_2.setText(_translate("Dialog", "钥匙ID", None))
        self.label_4.setText(_translate("Dialog", "钥匙编码", None))
        self.label_8.setText(_translate("Dialog", "开始时间", None))
        self.label_9.setText(_translate("Dialog", "结束时间", None))
        self.label_7.setText(_translate("Dialog", "周映射", None))
        self.label_3.setText(_translate("Dialog", "发生时间", None))

