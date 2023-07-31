from typing6 import KT, VT, ST, NumMapping, typing


#代表实数或布尔值之间映射的鸭子泛型。
class NumMappingProtocol(typing.Protocol[KT, VT, ST]):
    def __init__(self, data: dict[KT, VT]): ...

    def __getitem__(self, k: KT) -> VT: ...

    def __setitem__(self, k: KT, v: VT): ...

    def __delitem__(self, k: KT): ...

    def sum(self) -> ST: ...


#创建4个NumMapping的泛型别名。
type1 = NumMapping[int, bool, float]
type2 = NumMapping[int, bool, int]
type3 = NumMapping[float, bool, float]
type4 = NumMapping[float, bool, int]

#创建4个NumMappingProtocol的泛型别名。
protocol1 = NumMappingProtocol[int, bool, float]
protocol2 = NumMappingProtocol[int, bool, int]
protocol3 = NumMappingProtocol[float, bool, float]
protocol4 = NumMappingProtocol[float, bool, int]

#声明四个以不同泛型别名为类型注解的变量。
a: protocol1
b: protocol2
c: protocol3
d: protocol4

#验证不同泛型别名允许的子类型范围。
if __name__ == '__main__':
    a = type4({1.0: True, 0.0: False})
    a = type3({1.0: True, 0.0: False})
    a = type2({1: True, 0: False})
    a = type1({1: True, 0: False})

    b = type4({1.0: True, 0.0: False})
    b = type3({1.0: True, 0.0: False})    #报错。
    b = type2({1: True, 0: False})
    b = type1({1: True, 0: False})    #报错。

    c = type4({1.0: True, 0.0: False})
    c = type3({1.0: True, 0.0: False})
    c = type2({1: True, 0: False})    #报错。
    c = type1({1: True, 0: False})    #报错。

    d = type4({1.0: True, 0.0: False})
    d = type3({1.0: True, 0.0: False})    #报错。
    d = type2({1: True, 0: False})    #报错。
    d = type1({1: True, 0: False})    #报错。
