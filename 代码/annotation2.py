import random
import typing

#该全局变量的标注说明它应该引用一个浮点数。
m: float = 1.0


#定义一个函数，该函数本身没有标注，但其内的本地变量具有标注。
def arith_seq(n):
    #声明m是全局变量。这里不能有标注。
    global m

    #该本地变量的标注说明它应该引用一个整数。
    start: int = random.randrange(3)

    #该本地变量的标注说明它应该引用一个整数列表。
    seq: list[int] = []

    #for语句中的变量不能有标注，故只能将标注单独写一行。  i的标注说明它应该引用一个
    # 复数，但被赋值整数，不符合其标注。
    i: complex
    for i in range(n):
        #seq被添加浮点数，不符合其标注。
        seq.append(start + i*m)

    def result():
        #声明seq是外层本地变量。这里不能有标注。
        nonlocal seq
        print(seq)

    return result


#m的标注被修改，但这在类型检查中会被视为错误，不起作用。
m: complex
#m被赋值一个复数，不符合其标注。
m = 2 + 0j


#定义一个类。
class GeoSeq():
    #该类变量的标注说明它应该引用一个浮点数，且被所有GeoSeq类的对象共享。
    #  它被赋值一个复数，不符合其标注。
    m: typing.ClassVar[float] = m

    #该类变量的标注说明它应该引用一个整数，且被当成同名实例变量的默认值使用。
    start: int = 1

    #__init__方法中的本地变量就是实例变量。
    def __init__(self, n):
        #该实例变量的标注说明它应该引用一个整数。
        self.n: int = n
        #该实例变量的标注说明它应该引用一个整数。
        self.start: int = random.randrange(3)
        if self.start == 0:
            self.start = GeoSeq.start

    #该方法中的本地变量也有标注。
    def __enter__(self):
        #该本地变量的标注说明它应该引用一个浮点数列表。
        seq: list[float] = []
        #同样，for语句中的变量不能有标注。  i的标注说明它应该引用一个整数。
        i: int
        for i in range(self.n):
           seq.append(self.start * GeoSeq.m**i)
        return seq

    def __exit__(self, exc_type, exc_value, traceback):
        return False


#显示等差数列。
f = arith_seq(5)
f()

#显示等比数列。
o = GeoSeq(5)
#with语句中的变量不能有标注，故只能将标注单独写一行。  result的标注说明它应该引用一个
# 字符串列表，但实际被赋值一个复数列表，不符合其标注。
result: list[str]
with o as result:
    #解包赋值中的变量不能有标注，故只能分别将每个变量的标注单独写一行。  这些变量标注
    # 说明它们都应引用一个浮点数，但实际都被赋值一个复数，不符合其标注。
    a1: float
    a2: float
    a3: float
    a4: float
    a5: float
    a1, a2, a3, a4, a5 = result
    print(f"[{a1}, {a2}, {a3}, {a4}, {a5}]")
