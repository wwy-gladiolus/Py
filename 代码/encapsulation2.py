#此数据描述器用于保证托管属性引用一个浮点数。
class FloatValidator:
    #用该描述器本身的实例属性managed储存被托管属性的名称_name。  而name就是引用该
    # 描述器的公有属性的名称。
    def __set_name__(self, owner, name):
        self.managed = '_' + name

    #当通过实例读取name属性时，转化为读取_name属性。  当通过类对象读取name属性时，
    # 返回描述器本身。  读取到的浮点数保留两位小数。
    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        else:
            value = getattr(instance, self.managed, NotImplemented)
            if value is not NotImplemented:
                value = round(value, 2)
            return value

    #当通过实例设置name属性时，转化为设置_name属性。  设置时要保证赋值浮点数，默认
    # 为0.0。
    def __set__(self, instance, value):
        try:
            value = float(value)
        except ValueError:
            value = 0.0
        setattr(instance, self.managed, value)

    #当通过实例删除name属性时，转化为删除_name属性。
    def __delete__(self, instance):
        delattr(instance, self.managed)


class Person:
    #访问托管属性_height的接口。
    height = FloatValidator()

    #访问托管属性_weight的接口。
    weight = FloatValidator()

    #初始化。
    def __init__(self, h, w):
        self.height = h
        self.weight = w


class Wallet:
    #访问托管属性_coin的接口。
    amount = FloatValidator()

    #初始化。
    def __init__(self):
        self.amount = 0.0

