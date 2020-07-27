from testDialog import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from testDialog import Ui_Dialog

class testDiaog(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)#像自己在日自己
        self.ui.pushButton_2.clicked.connect(self.PushButtonClicked2)

    def PushButton1Clicked(self):
        box = QtWidgets.QMessageBox()
        box.warning(self,"提示","这是一个按钮事件")

    def PushButtonClicked2(self):
        # self.close() #关闭
        box = QtWidgets.QMessageBox()
        box.warning(self, "提示", "这是第二个按钮")

    #
    # def PushButtonClicked2(self):
    #     self.close() #关闭

import sys
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = testDiaog()
    window.show()
    sys.exit(app.exec_())


