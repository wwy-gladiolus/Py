import functools

#定义一个代表扑克牌的类。
@functools.total_ordering
class Pocker:
    #添加了如下实例属性：
    #  suit：扑克牌的花色，用1～4分别表示黑桃、红桃、梅花和方块。
    #  rank：扑克牌的位阶，用1～13分别表示A、2～10和J、Q、K。
    def __init__(self, suit, rank):
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

    #显示一张扑克的花色和位阶。
    def show(self):
        #识别花色。
        if self.suit == 1:
            s = 'Spade'
        elif self.suit == 2:
            s = 'Heart'
        elif self.suit == 3:
            s = 'Club'
        else:
            s = 'Diamond'
        #识别位阶。
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
        #输出结果。
        print(s)

    #两张扑克相等的规则是花色和位阶都相同。
    def __eq__(self, other):
        if self.suit == other.suit and self.rank == other.rank:
            return True
        else:
            return False

    #扑克排序的规则是先比较位阶再比较花色。
    def __lt__(self, other):
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

