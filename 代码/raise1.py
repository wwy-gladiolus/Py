import math

tn = 0
vn = 0
zn = 0

def f(x, y):
    global tn, vn, zn
    try:
        try:
            result = math.nan
            result = math.sqrt(x)/y
        except TypeError:
            tn = tn + 1
            raise
        except ValueError:
            vn = vn + 1
            raise
        except ZeroDivisionError:
            zn = zn + 1
            raise
    except Exception:
        print('tn:' + str(tn) + ', vn:' + str(vn) + ', zn:' + str(zn))
    finally:
        return result
