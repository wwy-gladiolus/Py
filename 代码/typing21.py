from typing import NewType, Tuple

#创建Tuple[str, int]的一个子类，并将其命名为Record。
Record = NewType('Record', Tuple[str, int])

#创建Record的一个子类，并将其命名为Item。
Item = NewType('Item', Record)


#该函数需被传入一个Record类型或其子类型的对象。
def show_record(data: Record):
    print(data)


#t1是Tuple[str, int]类型。
t1 = ('abc', 0)
#t2是Record类型。
t2 = Record(t1)
#t3是Item类型。
t3 = Item(t2)
#显示True，说明t2和t1引用同一个对象。
print(t2 is t1)
#显示True，说明t3和t2引用同一个对象。
print(t3 is t2)

#传入Tuple[str, int]类型对象，报错。
show_record(t1)
#传入Record类型对象，不报错。
show_record(t2)
#传入Record的子类型对象，不报错。
show_record(t3)

