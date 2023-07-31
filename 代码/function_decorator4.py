from functools import wraps


#定义一个生成装饰器的函数。
def mydecorator_generator(
        before_action=lambda *args, **kwargs: print("I can do anything before calling the target!"), 
        after_action=lambda *args, **kwargs: print("I can do anything after calling the target!")):
    def mydecorator(wrapped):
        @wraps(wrapped)
        def wrapper(*args, **kwargs):
            before_action(*args, **kwargs)
            result = wrapped(*args, **kwargs)
            after_action(*args, **kwargs)
            return result
        return wrapper
    return mydecorator


#定义目标函数1，同时完成装饰。
@mydecorator_generator()
def mytarget1():
    print("I am doing nothing.")
    return 0


#定义目标函数2，同时完成装饰。
@mydecorator_generator(
        lambda *args, **kwargs: None,
        lambda *args, **kwargs: None)
def mytarget2(obj):
    print("I am doing the truth value testing.")
    return bool(obj)


#定义目标函数3，同时完成装饰。
@mydecorator_generator(
        lambda *args, **kwargs: None,
        lambda *args, **kwargs: print("The expression calculated is: " + str(float(args[0])) + "+" + str(float(args[1]))))
def mytarget3(x, y):
    print("I am an adder.")
    return float(x) + float(y)


#定义目标函数4，同时完成装饰。
@mydecorator_generator(
        lambda *args, **kwargs: print("Having received " + str(len(args)) + " strings!"),
        lambda *args, **kwargs: None)
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

