from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class Squiggly(QWidget):
    textChanged = pyqtSignal(str)
    def __init__(self, parent=None):
        super(Squiggly, self).__init__(parent)
        font = self.font()
        font.setPointSize(font.pointSize() + 20)
        self.setFont(font)
        self.text = QString("Squiggly")
        self.step = 0
        self.setWindowTitle("Squiggly")
        self.resize(360, 150)
        self.timer = QBasicTimer()
        self.timer.start(60, self)

    def timerEvent(self, event):
        if (event.timerId() == self.timer.timerId()):
            self.step += 1
            self.update()
        else:
            super(Squiggly, self).timerEvent(event)

    def paintEvent(self, event):
        sines = (0, 38, 71, 92, 100, 92, 71, 38, 0, -38, -71, -92, -100, -92, -71, -38)
        fm = QFontMetrics(self.font())
        x = (self.width() - fm.width(self.text)) / 2
        y = (self.height() + fm.ascent() - fm.descent()) / 2
        color = QColor()
        painter = QPainter(self)
        for i in range(self.text.size()):
            index = (self.step + i) % 16
            color.setHsv((15 - index)*16, 255, 191)
            painter.setPen(color)
            painter.drawText(x, y - ((sines[index]*fm.height()) / 400), self.text[i])
            x += fm.width(self.text[i])

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Q, Qt.Key_X, Qt.Key_Escape):
            self.close()
        else:
            super(Squiggly, self).keyPressEvent(event)
    def mousePressEvent(self, event):
        text, ok = QInputDialog.getText(self, "Squiggly - Set Text", "Text:",
        QLineEdit.Normal, self.text)
        if ok and not text.isEmpty():
            self.text = text
            self.update()
            self.textChanged.emit(self.text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    squiggly = Squiggly()
    squiggly.show()
    app.exec_()