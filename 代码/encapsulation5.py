import time
import functools


class CachedFibonacci:
    #以实例属性储存斐波拉契序列的索引。
    def __init__(self, i):
        self.index = i

    #斐波拉契序列生成器，私有类属性。
    def __fibonacci(self, n):
        if n < 2:
            return 1
        else:
            return self.__fibonacci(n-1) + self.__fibonacci(n-2)

    #基于实例属性动态生成斐波拉契序列的元素。  这虽然是一个类属性，但通过不同实例访
    # 问得到不同的值。
    @functools.cached_property
    def element(self):
        return self.__fibonacci(self.index)


#定义一个统计访问CachedFibonacci实例的element属性所需时间的函数。
def process_time(cf):
    starttime = time.time()
    print('element: ' + str(cf.element))
    endtime = time.time()
    print('time: ' + str(endtime - starttime))

