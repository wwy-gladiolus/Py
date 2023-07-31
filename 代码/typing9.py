from typing import TypeVar, TypedDict, Generic

T = TypeVar('T')


#声明一个属于泛型的TypedDict类型。
class Group(TypedDict, Generic[T]):
    leader: T
    members: list[T]


class Person():
    pass


#创建泛型别名。
PersonGroup = Group[Person]

p1 = Person()
p2 = Person()

pg1 = PersonGroup(leader=p1, members=[p1, p2])
pg2 = PersonGroup(leader=p1, members=p2)    #报错。

print(pg1)
print(pg2)

