import typing


class A:
    #该方法不能被重写。
    @typing.final
    def a(self):
        pass

    def b(self):
        pass


#该类不能作为其他类的基类。
@typing.final
class B(A):
    def a(self) -> int:    #报错。
        return 0

    def b(self) -> int:
        return 0


class C(B):    #报错。
    pass

