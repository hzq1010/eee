#coding=utf-8
#import random
#age = random.randint(1,100)
#print(age)
import time

question1=input('小精灵：您好，欢迎来到古灵阁，\n请问您需要帮助吗？需要or不需要？\n')
time.sleep(1)
if question1=='需要':
    question2=input('请问您需要什么帮助呢？1存取款；\n2货币兑换；3咨询\n')
    if question2=='1存取款':
        print('推荐你去存取款窗口')
    elif question2=='2货币兑换':
        question3=input('金加隆和人民币的兑换率\n为1:51.3，即一金加隆=51.3人民币\n请问您需要兑换多少金加隆呢？\n')
#        if question3==N:
        print('那么，您需要付给我'+str(float(question3)*51.3)+'人民币。')
    else:
        print('推荐你去咨询窗口。')
else:
    print('好的，再见。')

#print('那么，您需要付给我'+str(float(8)*51.3)+'人民币。')







