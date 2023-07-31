import typing

#代表实数或布尔值的逆变类型变量，它只被用作形式参数的类型注解。
KT = typing.TypeVar('KT', bound=typing.SupportsInt, contravariant=True)

#代表实数或布尔值的不变类型变量，它同时被用作形式参数和返回值的类型注解。
VT = typing.TypeVar('VT', bound=typing.SupportsInt)

#代表实数的协变类型变量，它只被用作返回值的类型注解。
ST = typing.TypeVar('ST', int, float, covariant=True)


#代表实数或布尔值之间映射的泛型。
class NumMapping(typing.Generic[KT, VT, ST]):
    default = False

    def __init__(self, data: dict[KT, VT]):
        for k, v in data.items():
            setattr(self, str(k), v)

    def __getitem__(self, k: KT) -> VT:
        #这里利用typing.cast()对self.default进行了强制类型转换。
        return getattr(self, str(k), typing.cast(VT, self.default))

    def __setitem__(self, k: KT, v: VT):
        setattr(self, str(k), v)

    def __delitem__(self, k: KT):
        delattr(self, str(k))

    def __repr__(self):
        s = ""
        for k, v in self.__dict__.items():
            if k[0] != "_":
                s += k + ": " + str(v) + ", "
        return "{" + s.strip(", ") + "}"

    __str__ = __repr__

    #计算映射中所有值之和。
    def sum(self) -> ST:
        total = 0
        for k, v in self.__dict__.items():
            if k[0] != "_":
                total += getattr(self, k)
        return total


if __name__ == '__main__':
    #该赋值语句不会报错，因为int在KT的绑定中，而bool, int和float都在VT的绑定中。
    skm1 = NumMapping({1: True, 2: 2, 3: 3.0})
    #该赋值语句会报错，因为str不在KT的绑定中。
    skm2 = NumMapping({'1': True, '2': 2, '3': 3.0})
    #该赋值语句会报错，因为complex不在VT的绑定中。
    skm3 = NumMapping({1: 1j, 2: 2j, 3: 3j})

