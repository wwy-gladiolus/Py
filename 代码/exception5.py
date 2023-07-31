import math
import time


def f(x, y):
    try:
        return math.sqrt(x)/y
    except (TypeError, ValueError, ZeroDivisionError) as e:
        t = time.asctime()
        fd = open('err.log', 'a')
        fd.writelines((
                'time: ' + t + '\n',
                'type: ' + repr(type(e)) + '\n',
                'args: ' + repr(e.args) + '\n',
                '\n'))
        fd.close()
        return math.nan
