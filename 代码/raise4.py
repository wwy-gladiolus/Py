import math
import sys
import types

def f(x, y):
    try:
        return math.sqrt(x)/y
    except Exception:
        t, v, tb = sys.exc_info()
        new_tb = types.TracebackType(None, tb.tb_frame, 1, 1)
        if t == TypeError:
            E = RuntimeError('Please enter two numbers!')
            E.with_traceback(new_tb)
            raise E from None
        elif t == ValueError:
            E = RuntimeError('x must be non-negative!')
            E.with_traceback(new_tb)
            raise E from None
        else:
            E = RuntimeError('y cannot be 0!')
            E.with_traceback(new_tb)
            raise E from None

