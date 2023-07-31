from typing import cast, Tuple, TypeVar, TypeVarTuple, Unpack

T = TypeVar('T', bound=float)

#定义类型变量元组。
Ts = TypeVarTuple('Ts')

#定义一个代表元组的类型，该元组至少有一个元素，且第一元素必须是浮点数。
TT = Tuple[T, *Ts]
#兼容Python 3.10的写法。
#TT = Tuple[T, Unpack[Ts]]


def sum(data: TT) -> T:
    x = cast(T, 0)
    for y in data:
        x += y
    return x


if __name__ == "__main__":
    print(sum((0, 1.5, True)))
    print(sum(tuple()))    #报错。
    print(sum((1j, 2j)))    #报错。
