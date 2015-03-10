# ! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Administrator'

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys

try:
    due = QTime.currentTime()
    message = "Alert"
    if len(sys.argv) < 2:
        raise ValueError
    hours, mins = sys.argv[1].split(":")
    due = QTime(int(hours),int(mins))
    if not due.isValid():
        raise ValueError
    if len(sys.argv) > 2:
        messege = " ".join(sys.argv[2:])
except ValueError:
    message = "aksdjfkdfj"
app = QApplication(sys.argv)

label = QLabel("<font color=red size=72><b>" + message+"</b></font>")
label.setWindowFlags(Qt.SplashScreen)
label.show()

QTimer.singleShot(60000, app.quit)

app.exec_()