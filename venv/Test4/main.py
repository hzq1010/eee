#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Py40 PyQt5 tutorial

In this example, we connect a signal
of a QSlider to a slot of a QLCDNumber.

author: Jan Bodnar
website: py40.com
last edited: January 2015
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication,QMainWindow)
from PyQt5 import QtWidgets
import test


class MainCode(QMainWindow, test.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        test.Ui_MainWindow.__init__(self)
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = MainCode()
    myshow.show()
    sys.exit(app.exec_())