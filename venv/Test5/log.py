from functools import wraps
import datetime

def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args,**kwargs):
            log_string = func.__name__ +"was called"
            # curr_time = datetime.datetime.now()
            # time_str = datetime.datetime.strftime(curr_time,'%Y-%m-%d %H:%M:%S.%f')
            # print(log_string)
            #打开logfile，并写入内容
            time_str = datetime.datetime.now().__str__()
            with open(logfile,'a') as opened_file:
                opened_file.write(time_str+':'+log_string+'\n')
                return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator

@logit()
def myfunc1():
    print("打印日志")
for x in range(1,10):
    myfunc1()