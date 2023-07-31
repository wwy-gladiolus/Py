import typing
from numbers import Number
from collections.abc import ByteString

U = typing.Union[int, float, complex]

#该函数实现了特定多态。
@typing.overload    #注册add()的第一个实现。
def add(x: U, y: U) -> U: ...
@typing.overload    #注册add()的第二个实现。
def add(x: str, y: str) -> str: ...
@typing.overload    #注册add()的第三个实现。
def add(x: ByteString, y: ByteString) -> ByteString: ...
def add(x, y):    #定义add()。
    #return x + y
    #add()的第一个实现。
    if isinstance(x, Number) and isinstance(y, Number):
        return x + y
    #add()的第二个实现。
    elif isinstance(x, str) and isinstance(y, str):
        return "".join([x, y])
    #add()的第三个实现。
    elif isinstance(x, ByteString) and isinstance(y, ByteString):
        if isinstance(x, bytes): 
            return b"".join([x, y])
        else:
            return bytearray(b"").join([x, y])
    #当实际参数的类型组合不匹配任何一个实现时，抛出TypeError异常。
    else:
        raise TypeError


if __name__ == "__main__":
    print(add(0, 15))
    print(add(8j, 6-9j))
    print(add('a', 'b'))
    print(add(b'a', b'b'))
    print(add(b'a', bytearray(b'b')))
    print(add(bytearray(b'a'), bytearray(b'b')))
    print(add('a', b'b'))
