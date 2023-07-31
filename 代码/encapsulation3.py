class Wallet:
    #在初始化时设置被托管的私有属性。
    def __init__(self):
        self._amount = 0.0

    #传入fget的函数。
    def get_amount(self):
        if self._amount is not NotImplemented:
            return round(self._amount, 2)
        else:
            return self._amount

    #传入fset的函数。
    def set_amount(self, value):
        try:
            value = float(value)
        except ValueError:
            value = 0.0
        self._amount = value

    #传入fdel的函数。
    def del_amount(self):
        self._amount = NotImplemented

    #作为访问私有属性接口的公有属性。
    amount = property(get_amount, set_amount, del_amount)

