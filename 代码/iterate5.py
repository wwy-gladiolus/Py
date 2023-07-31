#本脚本自定义一个迭代器类。
class MyIterator:
    def __init__(self, n):
        self.max_n = int(n)
        self.n = 0

    #满足迭代器协议对__iter__的要求。
    def __iter__(self):
        return self

    #满足迭代器协议对__next__的要求。
    def __next__(self):
        if self.n >= self.max_n:
            raise StopIteration()
        self.n += 1
        return self.n
