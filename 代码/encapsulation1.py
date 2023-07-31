class Grade:
    #实例属性_value的取值范围是1~5，只能取整数。
    def __init__(self, v):
        v = int(v)
        if v > 5:
            v = 5
        if v < 1:
            v = 1
        self._value = v

    #读取_value属性的方法。
    def getV(self):
        return self._value

    #设置_value属性的方法。  用同__init__的方法确保取值范围是1~5，只能取整数。
    def setV(self, v):
        v = int(v)
        if v > 5:
            v = 5
        if v < 1:
            v = 1
        self._value = v

    #删除_value属性的方法。  直接返回以禁止删除_value。
    def deleteV(self):
        return

