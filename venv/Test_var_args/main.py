def test_var_args(f,*argv):
    print(f)
    for arg in argv:
        print("*argv",arg)

def greet_me(**kwargs):
    for key,value in kwargs.items():
        print("{0} == {1}".format(key,value))

def test(arg1,arg2,arg3):
    print(arg1)
    print(arg2)
    print(arg3)

def iters(*args):

    return iter(args)



if __name__ == '__main__':
    test_var_args('1','2','3')
    greet_me(name="1")
    fargs = 1
    args = ("1sdjkf1")
    kwargs = {"arg1":22,"arg2":33,"arg3":44}
    test(**kwargs)

    my_string ="stringdhsgk12184"
    next1 = iters(my_string)
    print(next(next1))

    a = [(1,2),(4,1),(9,10),(13,-3)]
    a.sort(key=lambda x:x[1])

    print(a)

    print('----------------------')

    # 列表并行排序
    list1 = [5, 2, 4]
    list2 = [2, 6, 9]
    data = list(zip(list1, list2))
    data.sort()
    list1, list2 = map(lambda t: list(t), zip(*data))


    for n in range(2,1000):
        for x in range(2,n):
            if n%x==0:
                # print(n,'equal',x,'*',n/x)
                break
        else:
            # print(n,'is a prime number')
            break
    for n in range(2,100):
        for x in range(2,n):
            if n%x!=0:
                print(x,'is a prime number11')
