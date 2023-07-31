#定义一个代表北欧符文的类。
class Rune:
    #初始化时设置了如下实例属性：
    #  salutation: 符文的称呼，常量。
    #  pronunciation: 符文的发音，常量。
    #  number: 该符文的当前数量，变量。
    def __init__(self, s, p, n):
        self.salutation = s
        self.pronunciation = p
        self.number = n
    
    #重写__setattr__使得只能修改number属性，且无法添加其他实例属性。
    def __setattr__(self, name, value):
        #只允许设置salutation属性和pronunciation属性一次。
        if name == 'salutation' or name == 'pronunciation':
            if name in self.__dict__:
                return None
        #不允许设置未在__init__中添加的属性。
        elif name != 'number':
            return None
        else:
            pass
        object.__setattr__(self, name, value)

    #重写__delattr__使得无法删除实例属性。
    def __delattr__(self, name):
        return None

