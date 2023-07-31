import collections

#该类继承了collections模块定义的UserDict类，使得自定义映射类型变得简单。
class MyDict(collections.UserDict):
    def __init__(self, initialdata):
        self.data = collections.UserDict(initialdata)

    def __missing__(self, key):
        return "Unmatched key: " + str(key)

