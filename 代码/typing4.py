import typing


#定义一个鸭子类型Container。
@typing.runtime_checkable
class Container(typing.Protocol):
    def __len__(self) -> int:
        pass

    def __contains__(self, ele) -> bool:
        pass


class Example1():
    def __len__(self):
        return 0

    def __contains__(self, ele):
        return False


class Example2():
    def __len__(self):
        return 0

    def __contains__(self):
        return False

