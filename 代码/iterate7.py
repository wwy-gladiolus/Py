class MyIterable:
    def __init__(self, seq):
        self.data = seq

    class EvenIterator():
        def __init__(self, data):
            self.data = data
            self.length = len(data)
            self.index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.index >= self.length:
                raise StopIteration()
            ele = self.data[self.index]
            self.index += 2
            return ele

    #方向相反的迭代器的类型。
    class ReverseEvenIterator():
        def __init__(self, data):
            self.data = data
            self.length = len(data)
            self.index = (self.length-1)//2*2

        def __iter__(self):
            return self

        def __next__(self):
            if self.index < 0:
                raise StopIteration()
            ele = self.data[self.index]
            self.index -= 2
            return ele

    def __iter__(self):
        return self.EvenIterator(self.data)

    #返回方向相反的迭代器。
    def __reversed__(self):
        return self.ReverseEvenIterator(self.data)

