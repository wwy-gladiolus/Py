from functools import wraps


def mydecorator(wrapped):
    @wraps(wrapped)
    def wrapper(*args, **kwargs):
        print("I can do anything before calling the target!")
        result = wrapped(*args, **kwargs)
        print("I can do anything after calling the target!")
        return result
    return wrapper


@mydecorator
def mytarget1():
    print("I am doing nothing.")
    return 0


@mydecorator
def mytarget2(obj):
    print("I am doing the truth value testing.")
    return bool(obj)


@mydecorator
def mytarget3(x, y):
    print("I am an adder.")
    return float(x) + float(y)


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

