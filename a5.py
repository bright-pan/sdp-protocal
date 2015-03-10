#coding=utf-8

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class MyDlg(QDialog):
    def __init__(self, parent=None):
        super(MyDlg, self).__init__(parent)

        self.setWindowTitle("MessgeBox")
        self.label = QLabel("About MessgeBox")

        questionButton = QPushButton("Question")
        informationButton = QPushButton("Information")
        warningButton = QPushButton("Warning")
        criticalButton = QPushButton("Critical")
        aboutButton = QPushButton("About")
        aboutqtButton = QPushButton("About Qt")
        customButton = QPushButton("Custom")

        layout = QGridLayout()
        layout.addWidget(self.label, 0, 0, 1,2)
        layout.addWidget(questionButton, 1,0)
        layout.addWidget(informationButton, 1,1)
        layout.addWidget(warningButton, 2,0)
        layout.addWidget(criticalButton,2,1)
        layout.addWidget(aboutButton, 3,0)
        layout.addWidget(aboutqtButton, 3,1)
        layout.addWidget(customButton, 4,0)
        self.setLayout(layout)
        questionButton.clicked.connect(self.questionSlot)
        informationButton.clicked.connect(self.informationSlot)
        warningButton.clicked.connect(self.warningSlot)
        criticalButton.clicked.connect(self.criticalSlot)
        aboutButton.clicked.connect(self.aboutSlot)
        aboutqtButton.clicked.connect(self.aboutqtSlot)
        customButton.clicked.connect(self.customSlot)
    def questionSlot(self):
        button = QMessageBox.question(self, "Question", self.tr("已到达文件尾部，是否从头查找"),
                                      QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
        if button == QMessageBox.Ok:
            self.label.setText("Question button/Ok")
        elif button == QMessageBox.Cancel:
            self.label.setText("Question button/Cancel")
        else:
            return

    def informationSlot(self):
        QMessageBox.information(self, "Information", self.tr("填写任意信息"))
        self.label.setText("Information MessageBox")

    def warningSlot(self):
        button = QMessageBox.warning(self, "Warning", self.tr("是否需要？"),
                            QMessageBox.Save|QMessageBox.Discard,
                            QMessageBox.Save)
        if button == QMessageBox.Save:
            self.label.setText("Save")
        elif button == QMessageBox.Discard:
            self.label.setText("Discard")
        elif button == QMessageBox.Cancel:
            self.label.setText("cancel")
        else:
            return
    def criticalSlot(self):
        QMessageBox.critical(self, "Critical", self.tr("致命错误"))
        self.label.setText("Critical")
    def aboutSlot(self):
        QMessageBox.about(self,"About", self.tr("关于"))
        self.label.setText("About")
    def aboutqtSlot(self):
        QMessageBox.aboutQt(self, "About Qt")
        self.label.setText("About Qt MessageBox")
    def customSlot(self):
        customMB = QMessageBox(self)
        customMB.setWindowTitle("Custom Messge Box")
        lockButtom = customMB.addButton(self.tr("锁定"), QMessageBox.ActionRole)
        cancelButton=customMB.addButton("cancel",QMessageBox.ActionRole)
        customMB.setText("asfasdsafd")
        customMB.exec_()
        button = customMB.clickedButton()
        if button == lockButtom:
            self.label.setText("lock botton")
        elif button == cancelButton:
            self.label.setText("cancel botton")
        else:
            return
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mydlg = MyDlg()
    mydlg.show()
    sys.exit(app.exec_())