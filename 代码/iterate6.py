#本脚本自定义一个可迭代对象类。  它储存一个序列，但被迭代时只取得序列中的偶数项。
class MyIterable:
    def __init__(self, seq):
        self.data = seq

    #定义专属于该可迭代对象类型的迭代器类。
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

    #返回属于EvenIterator类型的迭代器。
    def __iter__(self):
        return self.EvenIterator(self.data)

