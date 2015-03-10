#coding=utf-8
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf-8"))

class MyDlg(QDialog):
    def __init__(self, parent=None):
        super(MyDlg, self).__init__(parent)

        self.setWindowTitle("MyDlg")
        file_pb = QPushButton(self.tr("文件对话框"))
        color_pb = QPushButton(self.tr("颜色对话框"))
        font_pb = QPushButton(self.tr("字体对话框"))

        self.fileLineEdit = QLineEdit()
        self.colorFrame=QFrame()
        self.colorFrame.setFrameShape(QFrame.Box)
        self.colorFrame.setAutoFillBackground(True)
        self.fontLineEdit=QLineEdit("Hello,world!")

        layout = QGridLayout()
        layout.addWidget(file_pb, 0,0)
        layout.addWidget(self.fileLineEdit, 0,1)
        layout.addWidget(color_pb, 1,0)
        layout.addWidget(self.colorFrame, 1,1)
        layout.addWidget(font_pb, 2,0)
        layout.addWidget(self.fontLineEdit, 2,1)
        self.setLayout(layout)

        self.connect(file_pb, SIGNAL("clicked()"), self.openFile)
        self.connect(color_pb, SIGNAL("clicked()"), self.openColor)
        self.connect(font_pb, SIGNAL("clicked()"), self.openFont)

    def openFile(self):
        s = QFileDialog.getOpenFileName(self,"Open file dialog","/","Python files(*.py)")
        self.fileLineEdit.setText(str(s))

    def openColor(self):
        c = QColorDialog.getColor(Qt.blue)
        if c.isValid():
            self.colorFrame.setPalette(QPalette(c))
    def openFont(self):
        f,ok=QFontDialog.getFont()
        if ok:
            self.fontLineEdit.setFont(f)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mydlg = MyDlg()
    mydlg.show()
    f = QFrame(mydlg)
    f.setStyleSheet("background-color: rgb(255, 0, 0);")
    f.show()
    sys.exit(app.exec_())