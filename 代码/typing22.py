import typing
from numbers import Number


def str_or_num(obj: str | int | float):
    print(typing.assert_type(obj, str | complex))    #报错。
    match obj:
        case str():
            #先报告obj的类型，再显示obj。
            print(typing.reveal_type(obj))
        case int():
            #先报告obj的类型，再显示obj。
            print(typing.reveal_type(obj))
        case _ as unreachable:
            try:
                typing.assert_never(unreachable)    #报错。
            except AssertionError:
                #先报告obj的类型，再显示obj。
                print(typing.reveal_type(obj))
    print("")


str_or_num("abc")
str_or_num(b"abc")    #报错。
str_or_num(0)
str_or_num(True)
str_or_num(1.3)
str_or_num(None)    #报错。

