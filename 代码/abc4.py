import collections.abc


#自定义一个类，它基于映射实现不可变序列的基本功能，但没有实现__reversed__、index()和
# count()。
class SeqExample1(collections.abc.Mapping):
    #基于一个映射设置序列，键值对转换为序列对象的实例属性，并自动计算和存储长度。
    def __init__(self, d):
        self.length = 0
        for k, v in d.items():
            setattr(self, k, v)
            self.length += 1

    #基于实例属性动态生成一个列表，然后返回该列表的迭代器。
    def __iter__(self):
        l = []
        for key in self.__dict__:
            if key[0] != "_" and key != "length":
                l.append(getattr(self, key))
        return iter(l)

    #返回储存的序列长度。
    def __len__(self):
        return self.length

    #将键转化为实例属性。
    def __getitem__(self, key):
        return getattr(self, key)


#自定义一个类，它继承了SeqExample1，额外实现了__reversed__、index()和count()。
class SeqExample2(SeqExample1):
    #基于实例属性动态生成一个列表，将其反向，然后返回该列表的迭代器。
    def __reversed__(self):
        l = []
        for key in self.__dict__:
            if key[0] != "_" and key != "length":
                l.append(getattr(self, key))
        l.reverse()
        return iter(l)

    #遍历实例属性以根据值查找键。
    def index(self, value):
        for key in self.__dict__:
            if key[0] != "_" and key != "length":
                if getattr(self, key) == value:
                    return key
        raise ValueError(f"{value} not in sequence")

    #搜索实例属性以计算值的出现次数。
    def count(self, value):
        n = 0
        for key in self.__dict__:
            if key[0] != "_" and key != "length":
                if getattr(self, key) == value:
                    n += 1
        return n



