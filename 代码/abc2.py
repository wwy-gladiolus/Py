import abc
import numbers
import math


#定义代表二元整型向量的类。
class BiIntVector():
    #定义一个取得二元整型向量实部的描述器。
    class Real:
        def __get__(self, instance, owner=None):
            if instance:
                return instance.x
            else:
                return self

    #定义一个取得二元整型向量虚部的描述器。
    class Imag:
        def __get__(self, instance, owner=None):
            if instance:
                return instance.y
            else:
                return self

    #初始化二元整型向量。
    def __init__(self, x, y):
        x = int(x)
        y = int(y)
        self.x = x
        self.y = y

    #将二元整型向量转换为字符串。
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    #取得二元整型向量的实部。
    real = Real()

    #取得二元整型向量的虚部。
    imag = Imag()

    #计算共轭二元整型向量，即将虚部设置为其相反数。
    def conjugate(self):
        return BiIntVector(self.x, -self.y)

    #将二元整型向量转换为复数，该复数的实部和虚部分别等于二元整型向量的实部和虚部。
    def __complex__(self):
        return complex(self.x, self.y)

    #计算二元整型向量的绝对值，即该向量的长度。
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    #对二元整型向量进行逻辑值检测，仅当其绝对值为0时才返回False，其他情况返回True。
    def __bool__(self):
        if self.__abs__() == 0:
            return False
        else:
            return True

    #实现二元整型向量之间的==和!=比较。
    def __eq__(self, other):
        if isinstance(other, BiIntVector):
            return self.x == other.x and self.y == other.y
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, BiIntVector):
            return self.x != other.x or self.y != other.y
        else:
            return NotImplemented

    #实现二元整型向量的加法，注意操作数必须都是二元整型向量。
    def __pos__(self):
        return self

    def __add__(self, other):
        if isinstance(other, BiIntVector):
            return BiIntVector(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, BiIntVector):
            return BiIntVector(other.x + self.x, other.y + self.y)
        else:
            return NotImplemented

    def __iadd__(self, other):
        print("augmented addition!")
        return self.__add__(other)

    #实现二元整型向量的减法，注意操作数必须都是二元整型向量。
    def __neg__(self):
        return BiIntVector(-self.x, -self.y)

    def __sub__(self, other):
        if isinstance(other, BiIntVector):
            return BiIntVector(self.x - other.x, self.y - other.y)
        else:
            return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, BiIntVector):
            return BiIntVector(other.x - self.x, other.y - self.y)
        else:
            return NotImplemented

    def __isub__(self, other):
        print("augmented subtraction!")
        return self.__sub__(other)

    #实现二元整型向量的乘法，注意操作数必须都是二元整型向量。
    def __mul__(self, other):
        if isinstance(other, BiIntVector):
            return BiIntVector(self.x * other.x, self.y * other.y)
        else:
            return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, BiIntVector):
            return BiIntVector(other.x * self.x, other.y * self.y)
        else:
            return NotImplemented

    def __imul__(self, other):
        print("augmented multiplication!")
        return self.__mul__(other)

    #实现二元整型向量的除法，注意操作数必须都是二元整型向量。
    def __truediv__(self, other):
        if isinstance(other, BiIntVector):
            return BiIntVector(self.x // other.x, self.y // other.y)
        else:
            return NotImplemented

    def __rtruediv__(self, other):
        if isinstance(other, BiIntVector):
            return BiIntVector(other.x // self.x, other.y // self.y)
        else:
            return NotImplemented

    def __itruediv__(self, other):
        print("augmented division!")
        return self.__truediv__(other)

    #实现二元整型向量的乘方，注意操作数必须都是二元整型向量。
    def __pow__(self, other):
        if isinstance(other, BiIntVector):
            return BiIntVector(self.x ** other.x, self.y ** other.y)
        else:
            return NotImplemented

    def __rpow__(self, other):
        if isinstance(other, BiIntVector):
            return BiIntVector(other.x ** self.x, other.y ** self.y)
        else:
            return NotImplemented

    def __ipow__(self, other):
        print("augmented power!")
        return self.__pow__(other)


#将BiIntVector注册为Complex的虚子类。
numbers.Complex.register(BiIntVector)

