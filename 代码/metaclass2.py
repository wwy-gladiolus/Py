#自定义映射。
class PrefixMapping(dict):
    def __init__(self, prefix):
        self.prefix = prefix

    def __setitem__(self, key, value):
        if key[0] != "_":
            dict.__setitem__(self, self.prefix + "_" + key, value)
        else:
            dict.__setitem__(self, key, value)


#定义元类。
class PrefixMeta(type):
    @classmethod
    def __prepare__(cls, name, bases, **kwds):
        return PrefixMapping(name)


#定义属于该元类的第一个类。
class A(metaclass=PrefixMeta):
    dimension = 2

    def __init__(self, x, y): 
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def location(self):
        print("(" + str(self.x) + ", " + str(self.y) + ")")


#定义属于该元类的第二个类。
class B(metaclass=PrefixMeta):
    dimension = 2

    def __init__(self, x, y): 
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def location(self):
        print("(" + str(self.x) + ", " + str(self.y) + ")")

