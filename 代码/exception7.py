import math
import time
import sys


def f(x, y):
    try:
        return math.sqrt(x)/y
    except (TypeError, ValueError, ZeroDivisionError):
        t = time.asctime()
        ty, v, tb = sys.exc_info()
        cursor = tb
        tb_info = ''
        while cursor is not None:
            tb_info = tb_info + repr(cursor.tb_frame) + '\n'
            cursor = cursor.tb_next
        fd = open('err.log', 'a')
        fd.writelines((
                'time: ' + t + '\n',
                'type: ' + repr(ty) + '\n',
                'args: ' + repr(v.args) + '\n',
                'traceback:\n',
                tb_info,
                '\n'))
        fd.close()
        return math.nan
