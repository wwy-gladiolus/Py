#该函数包含如下参数:
# 仅位置参数op取如下字符串来指定运算：
#   'add': 加法
#   'sub': 减法
#   'mult': 乘法
#   'div': 除法
# 位置或关键字参数x和y为两个操作数，取浮点数。
# 仅关键字参数floordiv取布尔值，以表明是否进行整除。
def arithmetic_calculator(op, /, x, y, *, floordiv):
    #确保两个操作数都是浮点数。
    x = float(x)
    y = float(y)

    #根据指定的运算返回相应结果。  如果指定的运算不能识别，则返回NotImplemented。
    if op == 'add':
        return x + y
    elif op == 'sub':
        return x - y
    elif op == 'mult':
        return x * y
    elif op == 'div':
        if floordiv:
            return x // y
        else:
            return x / y
    else:
        return NotImplemented

