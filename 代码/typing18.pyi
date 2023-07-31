import typing

NAME: typing.Final = "abc"

NAME = "def"    #报错

class C():
    NUM: typing.Final[int] = 3.0    #报错

C.NUM = 3    #报错
