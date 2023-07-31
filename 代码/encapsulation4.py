class Wallet:
    def __init__(self):
        self._amount = 0.0

    #在定义作为访问私有属性接口的公有属性的同时实现了fget。
    @property
    def amount(self):
        if self._amount is not NotImplemented:
            return round(self._amount, 2)
        else:
            return self._amount

    #更新fset。
    @amount.setter
    def amount(self, value):
        try:
            value = float(value)
        except ValueError:
            value = 0.0
        self._amount = value

    #更新fdel。
    @amount.deleter
    def amount(self):
        self._amount = NotImplemented

