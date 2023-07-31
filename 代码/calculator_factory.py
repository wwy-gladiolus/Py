#该函数包含如下参数:
# 位置或关键字参数op取如下字符串来指定操作类型:
#   'add': 加法。
#   'sub': 减法。
#   'mult': 乘法。
#   'div': 除法。
#   'bool': 逻辑值检测。
#   'not': 逻辑非。
#   'and': 逻辑与。
#   'or': 逻辑或。
#   'switch': ... if ... else ...。
# 仅关键字参数modifiers接收所有修饰符。可能的修饰符包括:
#   floordiv: 取布尔值，以表明是否进行整除，默认不进行。
#   boolean: 取布尔值，以表明对于二元和三元逻辑运算，是否将返回的对象转换为布尔值，
#  默认不转换。
def calculator_factory(op, **modifiers):
    if op == 'add':
        return lambda x, y: float(x) + float(y)
    elif op == 'sub':
        return lambda x, y: float(x) - float(y)
    elif op == 'mult':
        return lambda x, y: float(x) * float(y)
    elif op == 'div':
        if 'floordiv' in modifiers and modifiers['floordiv']:
            return lambda x, y: float(x) // float(y)
        else:
            return lambda x, y: float(x) / float(y)
    elif op == 'bool':
        return lambda x: bool(x)
    elif op == 'not':
        return lambda x: not x
    elif op == 'and':
        if 'boolean' in modifiers and modifiers['boolean']:
            return lambda x, y: bool(x and y)
        else:
            return lambda x, y: x and y
    elif op == 'or':
        if 'boolean' in modifiers and modifiers['boolean']:
            return lambda x, y: bool(x or y)
        else:
            return lambda x, y: x or y
    elif op == 'switch':
        if 'boolean' in modifiers and modifiers['boolean']:
            return lambda x, y, z: bool(x if y else z)
        else:
            return lambda x, y, z: x if y else z
    else:
        return NotImplemented

