from typing import Tuple, AnyStr


def record(name: AnyStr, data: AnyStr) -> Tuple[AnyStr, AnyStr]:
    return (name, data)


record("abc", "xyz")
record(b"abc", b"xyz")
record(bytearray(b"abc"), bytearray(b"xyz"))
record("abc", b"xyz")    #报错。
record("abc", bytearray(b"xyz"))    #报错。
record(b"abc", bytearray(b"xyz"))

