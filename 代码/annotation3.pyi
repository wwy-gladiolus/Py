import functools
import typing
import random

@functools.total_ordering
class Pocker:
    SPADE: str
    HEART: str
    CLUB: str
    DIAMOND: str
    
    def __init__(self, suit: typing.Annotated[int, range(1, 5)], rank: typing.Annotated[int, range(1, 14)]): ...

    def __repr__(self):...

    __str__ = __repr__

    #使用装饰器@typing.no_type_check以跳过静态类型检查。
    @typing.no_type_check
    def __eq__(self, other: "Pocker"): ...
        
    def __lt__(self, other: "Pocker"): ...


class Draw(Pocker):
    def __init__(self, who: str): ...

    def compare(self, other: "Draw") -> int: ...


if typing.TYPE_CHECKING:
    draw1 = Draw("Jimmy")
    draw2 = Draw("Nacy")
    draw3 = Draw(None)
    draw1.compare(draw2)
    print("")
    draw2.compare(draw3)
    print("")
    draw3.compare(draw1)
