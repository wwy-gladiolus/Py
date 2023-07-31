import typing
from collections.abc import Sequence

#定义一个既没有绑定也没有约束的类型变量。
T1 = typing.TypeVar('T1')
#定义一个有绑定的类型变量。
T2 = typing.TypeVar('T2', bound=Sequence)
#定义一个有约束的类型变量。
T3 = typing.TypeVar('T3', tuple, list)


def a(x: T1) -> T1:
    return x


def b(x: T2) -> T2:
    return x


def c(x: T3) -> T3:
    return x


#该函数调用不会报错，因为T1对类型无限制。
a((0, 10))
#该函数调用不会报错，因为tuple是T2的绑定的子类型。
b((0, 10))
#该函数调用不会报错，因为tuple在T3的约束中。
c((0, 10))
#该函数调用不会报错，因为T1对类型无限制。
a([0, 10])
#该函数调用不会报错，因为list是T2的绑定的子类型。
b([0, 10])
#该函数调用不会报错，因为list在T3的约束中。
c([0, 10])
#该函数调用不会报错，因为T1对类型无限制。
a(range(0, 10))
#该函数调用不会报错，因为range是T2的绑定的子类型。
b(range(0, 10))
#该函数调用会报错，因为range不在T3的约束中。
c(range(0, 10))
#该函数调用不会报错，因为T1对类型无限制。
a(0)
#该函数调用会报错，因为int不是T2的绑定的子类型。
b(0)
#该函数调用会报错，因为int不在T3的约束中。
c(0)

