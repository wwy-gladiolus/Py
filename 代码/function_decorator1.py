#定义被用作装饰器的函数。
def mydecorator(wrapped):
    def wrapper(*args, **kwargs):
        print("I can do anything before calling the target!")
        result = wrapped(*args, **kwargs)
        print("I can do anything after calling the target!")
        return result
    return wrapper


#定义目标函数1。
def mytarget1():
    print("I am doing nothing.")
    return 0


#定义目标函数2。
def mytarget2(obj):
    print("I am doing the truth value testing.")
    return bool(obj)


#定义目标函数3。
def mytarget3(x, y):
    print("I am an adder.")
    return float(x) + float(y)


#定义目标函数4。
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


#对目标函数1进行装饰。
mytarget1 = mydecorator(mytarget1)

#对目标函数2进行装饰。
mytarget2 = mydecorator(mytarget2)

#对目标函数3进行装饰。
mytarget3 = mydecorator(mytarget3)

#对目标函数4进行装饰。
mytarget4 = mydecorator(mytarget4)

