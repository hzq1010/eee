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
import Ui


class MainCode(QMainWindow, Ui.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # self.Slider.valueChanged.connect(self.Number.display)
        # self.Slider.valueChanged.connect(self.buttonClicked)
    # def change(self):
    #     return  self.Number.display

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = MainCode()
    myshow.show()
    sys.exit(app.exec_())