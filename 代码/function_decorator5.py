#定义被用作装饰器的类。
class mydecorator:
    def __init__(self, func):
        self.func = func
        self.__name__ = func.__name__
        self.__qualname__ = func.__qualname__
        self.__module__ = func.__module__
        self.__doc__ = func.__doc__
        self.__annotations__ = func.__annotations__
        self.__code__ = func.__code__
        self.__defaults__ = func.__defaults__
        self.__kwdefaults__ = func.__kwdefaults__
        self.__globals__ = func.__globals__
        self.__closure__ = func.__closure__

    def __call__(self, *args, **kwargs):
        print("I can do anything before calling the target!")
        result = self.func(*args, **kwargs)
        print("I can do anything after calling the target!")
        return result


#定义目标函数1，同时完成装饰。
@mydecorator
def mytarget1():
    print("I am doing nothing.")
    return 0


#定义目标函数2，同时完成装饰。
@mydecorator
def mytarget2(obj):
    print("I am doing the truth value testing.")
    return bool(obj)


#定义目标函数3，同时完成装饰。
@mydecorator
def mytarget3(x, y):
    print("I am an adder.")
    return float(x) + float(y)


#定义目标函数4，同时完成装饰。
@mydecorator
def mytarget4(*substr):
    print("I am an concatenator.")
    length = len(substr)
    if length == 0:
        return ''
    elif length == 1:
        return substr[0]
    else:
        i = 0
        s = ''
        while i < length:
            s = s + substr[i]
            i = i + 1
        return s

