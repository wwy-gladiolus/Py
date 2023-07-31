from typing import Protocol, Callable
from collections.abc import Sequence


#回调函数的类型为Callable[[int, int], float]。
def bubble_sort_int(lt: list, compare: Callable[[int, int], float]) -> list: ...


#回调函数的类型为Callable[[float, float], float]。
def bubble_sort_float(lt: list, compare: Callable[[float, float], float]) -> list: ...


#回调函数的类型为Callable[[str, str], float]。
def bubble_sort_str(lt: list, compare: Callable[[str, str], float]) -> list: ...


if __name__ == "__main__":
    #该函数的类型为Callable[[int, int], bool]。
    def f1(x: int, y: int) -> bool: ...


    #该函数的类型为Callable[[float, float], int]。
    def f2(x: float, y: float) -> int: ...


    #该函数的类型为Callable[[Sequence, Sequence], float]。
    def f3(x: Sequence, y: Sequence) -> float: ...


    bubble_sort_int(list(), f1)
    bubble_sort_int(list(), f2)
    bubble_sort_int(list(), f3)    #报错。

    bubble_sort_float(list(), f1)    #报错。
    bubble_sort_float(list(), f2)
    bubble_sort_float(list(), f3)    #报错。

    bubble_sort_str(list(), f1)    #报错
    bubble_sort_str(list(), f2)    #报错
    bubble_sort_str(list(), f3)
