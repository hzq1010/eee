# -*- coding: utf-8 -*-
import sys, random, time
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from guessNumberGame import Ui_Form

times = 1  # 声明一个模块内的全局变量；用于记录猜数字的次数
rand = 20  # 声明一个模块内的全局变量；神秘数字的最大范围
allTimes = 7  # 声明一个模块内的全局变量；游戏最大次数


class mwindow(QWidget, Ui_Form):
    def __init__(self):  # 初始化
        super(mwindow, self).__init__()  # 这是对继承自父类的属性进行初始化。而且是用父类的初始化方法来初始化继承的属性。
        self.setupUi(self)

    # 定义一个方法：从下拉框选择游戏难度
    def gameLevel(self):
        times = 1
        global rand, allTimes
        level = self.comboBox.currentIndex()
        if level == 0:
            rand = 20
            allTimes = 7
        if level == 1:
            rand = 30
            allTimes = 10
        if level == 2:
            rand = 50
            allTimes = 15
        if level == 3:
            rand = 100
            allTimes = 20

    # 定义一个方法：选择游戏难度后生成一个随机的神秘数字
    def getRandNum(self):
        global theNum, times
        times = 1  # 每次选择游戏难度并点击“确定”后，已猜数字次数都重新归为1
        w.pushButton.setEnabled(True)  # 设置pushButton可点击（即选择了游戏难度之后，pushButton才可点击）
        theNum = random.randint(1, rand)
        self.textBrowser.append('开始游戏吧，你有%d次机会，数字范围：1-%d' % (allTimes, rand))
        # self.textBrowser.append(str(theNum)) #直接显示神秘数字，用于调试时使用

    # 定义一个方法：点击“确定”按钮的事件，用于比较所猜数字和神秘数字
    def guess(self):
        global allTimes, times  # 使用全局变量times
        yourNum = int(self.lineEdit.text())  # 从文本框获取到输入的数字，并转化为int型
        if yourNum < theNum and times < allTimes:
            text = "你猜的数字%d小了！你还有%d次机会，再猜！" % (yourNum, allTimes - times)
            self.textBrowser.append(text)  # 把提示信息写入textBrowser
            times += 1
        elif yourNum > theNum and times < allTimes:
            text = "你猜的数字%d大了！你还有%d次机会，再猜！" % (yourNum, allTimes - times)
            self.textBrowser.append(text)
            times += 1
        elif yourNum == theNum and times < allTimes:
            text = '你猜对了，就是%d，你一共猜了%s次！' % (theNum, times)
            self.textBrowser.append(text)
        else:
            text = '%d次机会用完了你也没猜对！神秘数字其实是：%d' % (allTimes, theNum)
            self.textBrowser.append(text)

    # 定义一个方法：点击“再来一局”时触发的事件
    def reStart(self):
        self.textBrowser.clear()  # 清除textBrowser内的内容
        self.lineEdit.clear()  # 清除lineEdit内的内容
        w.pushButton.setEnabled(False)  # 设置pushButton不可点击（即在选择游戏难度之前，pushButton不可点击）


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mwindow()
    w.pushButton.setEnabled(False)  # 设置pushButton不可点击（即在选择游戏难度之前，pushButton不可点击）
    w.pushButton.clicked.connect(w.guess)  # 绑定guess方法
    w.pushButton_2.clicked.connect(w.getRandNum)
    w.comboBox.currentIndexChanged.connect(w.gameLevel)
    w.pushButton_3.clicked.connect(w.reStart)
    w.show()
    sys.exit(app.exec_())  # 使程序一直循环运行直到主窗口被关闭终止进程（如果没有这句话，程序运行时会一闪而