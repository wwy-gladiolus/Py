import math


c = 'c'

def f(x, y):
    global c
    a = 'a'
    try:
        b = 'b'
        return math.sqrt(x)/y 
    except TypeError as a:
        print(a)
        return math.nan
    except ValueError as b:
        print(b)
        return math.nan
    except ZeroDivisionError as c:
        print(c)
        return math.nan
    finally:
        print(a)
        print(b)
        print(c)

