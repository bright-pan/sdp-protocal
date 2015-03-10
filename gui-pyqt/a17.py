# ! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Administrator'

import sys
import urllib2

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        date = self.getdata()
        rates = sorted(self.rates.keys())

        dateLabel = QLabel(date)
        self.fromComboBox = QComboBox()
        self.fromComboBox.addItems(rates)
        self.fromSpinBOx = QSpinBox()
        self.fromSpinBOx.setRange(0.01, 100000000.00)
        self.fromSpinBOx.setValue(1.00)
        self.toComboBox = QComboBox()
        self.toComboBox.addItems(rates)
        self.toLabel = QLabel("1.00")

        layout = QGridLayout()
        layout.addWidget(dateLabel, 0,0)
        layout.addWidget(self.fromComboBox, 1,0)
        layout.addWidget(self.fromSpinBOx, 1,1)
        layout.addWidget(self.toComboBox, 2,0)
        layout.addWidget(self.toLabel, 2,1)
        self.setLayout(layout)

        self.fromComboBox.currentIndexChanged.connect(self.updateUi)
        self.fromSpinBOx.valueChanged.connect((self.updateUi))
        self.toComboBox.currentIndexChanged.connect(self.updateUi)

    def updateUi(self):
        to = unicode(self.toComboBox.currentText())
        from_ = unicode(self.fromComboBox.currentText())
        amount = (self.rates[from_]/self.rates[to] * self.fromSpinBOx.value())
        self.toLabel.setText("%0.2f" % amount)



    def getdata(self): # Idea taken from the Python Cookbook
        self.rates = {}
        try:
            date = "Unknown"
            fh = urllib2.urlopen("http://www.bankofcanada.ca"
            "/en/markets/csv/exchange_eng.csv")
            for line in fh:
                if not line or line.startswith(("#", "Closing ")):
                    continue
                fields = line.split(",")
                if line.startswith("Date "):
                    date = fields[-1]
                else:
                    try:
                        value = float(fields[-1])
                        self.rates[unicode(fields[0])] = value
                    except ValueError:
                        pass
            print self.rates
            return "Exchange Rates Date: " + date
        except Exception, e:
            return "Failed to download:\n%s" % e

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())