import functools
import typing
import random


#该类的实例代表扑克牌。
@functools.total_ordering
class Pocker:
    #下列类变量的标注说明它们都应该引用一个字符串。
    SPADE: str = "\u2664"
    HEART: str = "\u2661"
    CLUB: str = "\u2667"
    DIAMOND: str = "\u2662"
    
    #suit参数的标注说明它应该被传入一个1~4范围内的整数。  rank参数的标注说明它应该被传
    # 入一个1~13范围内的整数。  该方法创建了一张扑克牌。
    def __init__(self, suit: typing.Annotated[int, range(1, 5)], rank: typing.Annotated[int, range(1, 14)]):
        self.suit = int(suit)
        if self.suit > 4:
            self.suit = 4
        if self.suit < 1:
            self.suit = 1
        self.rank = int(rank)
        if self.rank > 13:
            self.rank = 13
        if self.rank < 1:
            self.rank = 1

    #该方法和下面的__str__用于显示扑克牌。
    def __repr__(self):
        if self.suit == 1:
            s = Pocker.SPADE
        elif self.suit == 2:
            s = Pocker.HEART
        elif self.suit == 3:
            s = Pocker.CLUB
        else:
            s = Pocker.DIAMOND
        if self.rank == 1:
            s = s + ' A'
        elif self.rank == 11:
            s = s + ' J'
        elif self.rank == 12:
            s = s + ' Q'
        elif self.rank == 13:
            s = s + ' K'
        else:
            s = s + ' ' + str(self.rank)
        return s

    __str__ = __repr__

    #other参数的标注说明它应该被传入另一个Pocker对象。  该方法支持扑克牌进行相等比较。
    def __eq__(self, other: "Pocker"):
        if self.suit == other.suit and self.rank == other.rank:
            return True
        else:
            return False

    #other参数的标注说明它应该被传入另一个Pocker对象。  该方法支持扑克牌进行顺序比较。
    def __lt__(self, other: "Pocker"):
        srank = self.rank
        if srank == 1:
            srank = 14
        orank = other.rank
        if orank == 1:
            orank = 14
        if srank < orank:
            return True
        elif srank > orank:
            return False
        else:
            if self.suit <= other.suit:
                return False
            else:
                return True


#该类的实例代表抽牌的动作。
class Draw(Pocker):
    #who参数的标注说明它应该被传入一个字符串。  该方法记录下来了谁（通过who传入的人名）
    # 抽中了哪张扑克牌。
    def __init__(self, who: str):
        self.who = who
        self.card = Pocker(random.randrange(1, 5), random.randrange(1, 14))

    #other参数的标注说明它应该被传入另一个Draw对象，返回值是整数。  该方法比较两次抽牌
    # 的结果，并判断谁获胜。
    def compare(self, other: "Draw") -> int:
        print(f"{self.who}'s card: {self.card}")
        print(f"{other.who}'s card: {other.card}")
        if self.card > other.card:
            print(f"{self.who} win!")
            return 1
        elif self.card < other.card:
            print(f"{other.who} win!")
            return -1
        else:
            print("A draw!")
            return 0


#仅当进行静态类型检测时执行。
if typing.TYPE_CHECKING:
    #三次抽牌。
    draw1 = Draw("Jimmy")
    draw2 = Draw("Nacy")
    #这次抽牌传入的人名是None，不符合标注。
    draw3 = Draw(None)
    #比较三次抽牌的结果。
    draw1.compare(draw2)
    print("")
    draw2.compare(draw3)
    print("")
    draw3.compare(draw1)


