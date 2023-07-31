class MyIterable:
    def __init__(self, seq):
        self.data = seq

    def __iter__(self):
        length = len(self.data)
        i = 0
        while i < length:
            yield self.data[i]
            i += 2

    def __reversed__(self):
        i = (len(self.data)-1)//2*2
        while i >= 0:
            yield self.data[i]
            i -= 2
