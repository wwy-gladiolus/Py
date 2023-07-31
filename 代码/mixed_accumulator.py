#该函数包含如下参数:
# 位置或关键字参数elements可以接收任意多个操作数，当进行数值累加时它们必须取数值，
#  当进行字符串拼接时它们必须取字符串。
# 仅关键字参数op取如下字符串来指定操作:
#   'sum': 累加。
#   'concat': 拼接。
# 仅关键字参数pre、suf和sep都用于拼接字符串，分别设置前缀、后缀和分隔符。
def mixed_accumulator(
        *elements, op='sum', 
        pre='', suf='', sep=''):

    #确保指定的操作合法。
    if op not in ('sum', 'concat'):
        return NotImplemented

    #当操作数个数小于2时直接返回结果。
    length = len(elements)
    if length == 0:
        return None
    if length == 1:
        return elements[0]

    #分别处理累加和拼接。
    if op == 'sum':
        n = 0
        i = 0
        while i < length:
            n = n + float(elements[i])
            i = i + 1
        return n
    else:
        s = pre
        i = 0
        while i < length-1:
            s = s + str(elements[i]) + sep
            i = i + 1
        return s + str(elements[length-1]) + suf

