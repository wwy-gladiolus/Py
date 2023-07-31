import typing
from collections.abc import Mapping, Sequence
from functools import singledispatch

U = typing.Union[str, bytes, bytearray]


#定义一个泛型函数。  参数obj的类型是泛型，决定分派的结果。  参数maxrow的类型是int，
# 与分派无关。
@singledispatch
def table_gen(obj, maxrow=5):
    return [(1, obj)]


#以第一种方式将针对Sequence的实现注册给泛型函数。
@table_gen.register
def _(obj: Sequence, maxrow=5):
    table = list()
    row = 1
    for ele in obj:
        table.append((row, ele))
        if row == maxrow:
            break
        row += 1
    return table


#以第二种方式将针对Mapping的实现注册给泛型函数。
@table_gen.register(Mapping)
def _(obj, maxrow=5):
    table = list()
    row = 1
    for k, v in obj.items():
        table.append((row, k, v))
        if row == maxrow:
            break
        row += 1
    return table


#以第三种方式将针对字符串和字节串的实现注册给泛型函数。
table_gen.register(U, lambda obj, maxrow: [(1, obj)])


if __name__ == "__main__":
    #调用泛型函数本身。
    print(table_gen(0j))
    #调用针对字符串和字节串的实现。
    print(table_gen('abc', 5))
    #调用针对Sequence的实现。
    print(table_gen([1.6, -8.2, 7.9, 5.4, -0.9], 3))
    #调用针对Mapping的实现。
    print(table_gen({'a': b'a', 'b': b'b'}))
    #调用泛型函数本身。
    print(table_gen({'x', 'y', 'z'}))
