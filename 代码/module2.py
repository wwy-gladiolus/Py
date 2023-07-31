#定义可导入变量列表。
__all__ = ['a', '_f2', 'C1', '_C2']

a = 1

_b = 100


def f1():
    return 'f1'


def _f2():
    return 'f2'


class C1():
    def echo(self):
        return 'C1'


class _C2():
    def echo(self):
        return 'C2'



