#定义元类。
class Singleton(type):
    #为属于该元类的每个类都添加类属性instance。
    def __init__(self, *args, **kwargs):
        self.instance = None
        super().__init__(*args, **kwargs)

    #检查属于该元类的类的instance属性，仅当它不是None时才允许实例化。
    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = super().__call__(*args, **kwargs)
        return self.instance


#定义第一个属于Singleton的类。
class A(metaclass=Singleton):
    def __init__(self, n, *args):
        self.a = n
        super().__init__(*args)


#定义第二个属于Singleton的类。
class B(metaclass=Singleton):
    def __init__(self, n, *args):
        self.b = n
        super().__init__(*args)


#定义第三个属于Singleton的类。  它同时以A和B为直接基类。
class C(A, B):
    def __init__(self, n, m, l):
        self.c = l
        super().__init__(n, m)

