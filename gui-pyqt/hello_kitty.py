from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

app = QApplication(sys.argv)
b= QPushButton("hello, kitty!")
app.getPe
b.show()
b.clicked.connect(app.quit)
#b.connect(b,SIGNAL("clicked()"), app, SLOT("quit()"))
app.exec_()