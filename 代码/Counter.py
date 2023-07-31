#本脚本定义了一个代表计数器的类。
class Counter:
    def __init__(self):
        self.n = 0

    #该属性实现计数，并在每次计数时执行指定的操作。
    def tik(self):
        self.n += 1
        return self.n

    #该属性重置计数器。
    def reset(self):
        self.n = 0
