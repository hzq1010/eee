
# -*- coding:utf-8 -*-
def duplicates(list):

  value =set([x for x in list if list.count(x) >1])
  return value

def hi(name="yasuo"):
    return "hi"+name



def logger(func):
    def wrapper(*args, **kw):
        print('我准备开始计算：{} 函数了:'.format(func.__name__))

        # 真正执行的是这行。
        func(*args, **kw)

        print('啊哈，我计算完啦。给自己加个鸡腿！！')
    return wrapper

@logger
def add(x, y):
    print('{} + {} = {}'.format(x, y, x+y))


from functools import wraps

def logit(func):

    @wraps(func)
    def with_logging(*args, **kwargs):

        print(func.__name__ + " was called")

        return func(*args, **kwargs)

    return with_logging

@logit
def addition_func1(x):
    """Do some math."""
    return x + x




if __name__ == '__main__':
    # some_list = ['a','b','c','b','a']
    # result1= addition_func1(5)
    # print(result1)
    # print('hello world')
    #
    #
    #
    # print('000000000000000000000000')


    c='测试2222'
    print(len(c.encode(encoding = "gbk")))
