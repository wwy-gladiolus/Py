from typing import Union, TypeVar

T = TypeVar('T', int, str, bytes)


#该函数的参数x和y，以及返回值的可能类型都是int、str和bytes，然而三者的类型并不需要是
# 一致的，而可以存在多种组合。  这导致无法用一个类型变量T来作为它们的类型注解，只能使
# 用Union结构。
#def add_concate(x: T, y: T) -> T:
def add_concate(x: Union[int, str, bytes], y: Union[int, str, bytes]) -> Union[int, str, bytes]:
    try:
        if isinstance(x, int):
            if isinstance(y, int):
                return x + y
            elif isinstance(y, str):
                return x * y
            elif isinstance(y, bytes) or isinstance(y, bytearray):
                return x * y
            else:
                raise TypeError("y is of bad type!")
        elif isinstance(x, str):
            if isinstance(y, int):
                return x * y
            elif isinstance(y, str):
                return x + y
            elif isinstance(y, bytes) or isinstance(y, bytearray):
                raise TypeError("x's type and y's type are inconsistent!")
            else:
                raise TypeError("y is of bad type!")
        elif isinstance(x, bytes) or isinstance(x, bytearray):
            if isinstance(y, int):
                return x * y
            elif isinstance(y, str):
                raise TypeError("x's type and y's type are inconsistent!")
            elif isinstance(y, bytes) or isinstance(y, bytearray):
                return x + y
            else:
                raise TypeError("y is of bad type!")
        else:
            raise TypeError("x is of bad type!")
    except TypeError as e:
        return e.args[0]


if __name__ == "__main__":
    print(add_concate(2, 3))
    #使用T时报错。
    print(add_concate(2, 'abc'))
    #使用T时报错。
    print(add_concate(2, b'abc'))
    #使用T时报错。
    print(add_concate(2, bytearray(b'abc')))
    #总是报错。
    print(add_concate(2, 3.0))
    print("")
    #使用T时报错。
    print(add_concate('xyz', 3))
    print(add_concate('xyz', 'abc'))
    #使用T时报错。
    print(add_concate('xyz', b'abc'))
    #使用T时报错。
    print(add_concate('xyz', bytearray(b'abc')))
    #总是报错。
    print(add_concate('xyz', 3.0))

