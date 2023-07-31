from typing import Callable, Any
import collections.abc


#该函数可以调用任何返回值类型为int的函数，并返回获得的返回值。  在正式执行之前，会先显
# 示即将执行的函数调用。
def verbose(func: Callable[..., int], *args, **kwargs) -> int:
    params = ""
    for v in args:
        params += str(v) + ", "
    for k, v in kwargs.items():
        params += str(k) + "=" + str(v)+", "
    print(f"executing {func.__name__}({params.strip(', ')})")
    return func(*args, **kwargs)


if __name__ == "__main__":
    #该函数的类型为Callable[[], bool]。
    def f1() -> bool:
        return True


    #该函数的类型为Callable[[int, int], int]。
    def f2(x: int, y: int) -> int:
        return x + y


    #该函数的类型为Callable[[float, float], float]。
    def f3(x: float, y: float) -> float:
        return x * y


    #该函数的类型为Callable[..., str]。
    def f4(n: int, s: str, sep: str = "") -> str:
        return (n * (s + sep)).rstrip(sep)


    #该函数的类型为Callable[..., list]。
    def f5(*args: Any, reverse: bool = False) -> list:
        l = [s for s in args]
        if reverse:
            l.reverse()
            return l
        else:
            return l


    print(verbose(f1))
    print("")
    print(verbose(f2, 12, 34))
    print("")
    print(verbose(f3, 3.6, -1.7))    #报错。
    print("")
    print(verbose(f4, 3, "abc", sep="@"))    #报错。
    print("")
    print(verbose(f5, False, None, 0, reverse=True))    #报错。

