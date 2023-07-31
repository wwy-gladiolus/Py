import types


#定义第一个元类。
class meta1(type):
    pass


#定义第二个元类。
class meta2(type):
    pass


#定义第三个元类。
class meta3(meta1, meta2):
    pass


#定义属于meta1的类。
class A(metaclass=meta1):
    pass


#定义属于meta2的类。
class B(metaclass=meta2):
    pass


#定义属于meta3的类。
class C(metaclass=meta3):
    pass


#由于A的元类是meta1，所以最近派生元类是meta1。
print(types.prepare_class("O", (A,), {"metaclass": meta1}))

#由于A的元类是meta1，meta2和meta1之间没有继承关系，所以发生元类冲突。
try:
    print(types.prepare_class("O", (A,), {"metaclass": meta2}))
except TypeError as e:
    print(repr(e))

#由于A的元类是meta1，而meta3是meta1的子类，所以最近派生元类是meta3。
print(types.prepare_class("O", (A,), {"metaclass": meta3}))

#由于A的元类是meta1，B的元类是meta2，所以发生元类冲突。
try:
    print(types.prepare_class("O", (A, B)))
except TypeError as e:
    print(repr(e))

#由于A的元类是meta1，C的元类是meta3，而meta3是meta1的子类，所以最近派生元类
# 是meta3。
print(types.prepare_class("O", (A, C)))

#由于B的元类是meta2，C的元类是meta3，而meta3是meta2的子类，所以最近派生元类
# 是meta3。
print(types.prepare_class("O", (B, C)))

#由于A的元类是meta1，B的元类是meta2，meta3同时是meta1和meta2的子类，所以最
# 近派生元类是meta3。
print(types.prepare_class("O", (A, B), {"metaclass": meta3}))

#下面三条语句说明选取最近派生元类的算法是依次两两比较。

#首先比较A的元类meta1和B的元类meta2，发生元类冲突，不再继续比较。
try:
    print(types.prepare_class("O", (A, B, C)))
except TypeError as e:
    print(repr(e))

#首先比较A的元类meta1和C的元类meta3，选中meta3，然后再比较meta3和B的元类meta2，
# 最后依然选中meta3。
print(types.prepare_class("O", (A, C, B)))

#首先比较C的元类meta3和A的元类meta1，选中meta3，然后再比较meta3和B的元类meta2，
# 最后依然选中meta3。
print(types.prepare_class("O", (C, A, B)))

#下面的语句说明通过metaclass关键字指定的元类将与第一个基类比较，且是首先被比较，因
# 此发生元类冲突
try:
    print(types.prepare_class("O", (A, C, B), {"metaclass": meta2}))
except TypeError as e:
    print(repr(e))

