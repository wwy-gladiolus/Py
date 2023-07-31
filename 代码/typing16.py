from typing import Any, Callable, ParamSpec, Concatenate
from functools import wraps

#定义一个参数规格变量。
P = ParamSpec('P')


#该装饰器将f(x, y, *, error)装饰为f(pos, neg, zero, y, *, error)。 
def decorator(wrapped: Callable[Concatenate[Any, P], int])\
        -> Callable[Concatenate[str, str, str, P], str]:
    #这里用到了ParamSpec对象的args属性和kwargs属性。
    @wraps(wrapped)
    def wrapper(pos: str, neg: str, zero: str, *args: P.args, **kwargs: P.kwargs) -> str:
        try:
            match wrapped(0, *args, **kwargs):
                case 1:
                    return f"{args[0]} is {pos}."
                case -1:
                    return f"{args[0]} is {neg}."
                case _:
                    return f"{args[0]} is {zero}."
        except Exception as e:
            if e == kwargs["error"]:
                return e.args[0]
            else:
                raise
    return wrapper


#定义compare(x, y, *, error)，然后将其装饰为compare(pos, neg, zero, y, *,
# error)。
@decorator
def compare(x: Any, y: Any, *, error: Exception = RuntimeError()) -> int:
    try:
        if y > x:
            return 1
        elif y < x:
            return -1
        else:
            return 0
    except Exception:
        raise error


if __name__ == "__main__":
    print(compare('positive', 'negative', 'zero', 83.2, error=Exception("Not comparable!")))
    print(compare('positive', 'negative', 'zero', -19, error=Exception("Not comparable!")))
    print(compare('positive', 'negative', 'zero', 0, error=Exception("Not comparable!")))
    print(compare('positive', 'negative', 'zero', 0j, error=Exception("Not comparable!")))
    print(compare('+', '-', '0', 18, error=Exception("Not comparable!")))
    print(compare('+', '-', '0', -23.9, error=Exception("Not comparable!")))
    print(compare('+', '-', '0', -0.0, error=Exception("Not comparable!")))
    print(compare('+', '-', '0', 1+9j, error=Exception("Not comparable!")))

