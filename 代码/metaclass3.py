import types


#定义元类。
class ConstantMeta(type):
    @staticmethod
    def __new__(cls, name, bases, dic, **kwds):
        new_dic = {}
        for k, v in dic.items():
            if isinstance(v, types.FunctionType) or k[0] == '_':
                new_dic[k] = v
            else:
                new_dic[k.upper()] = v
        return type.__new__(cls, name, bases, new_dic, **kwds)


#定义属于该元类的类。
class Point(metaclass=ConstantMeta):
    dimension = 2

    def __init__(self, x, y): 
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def location(self):
        print("(" + str(self.x) + ", " + str(self.y) + ")")

