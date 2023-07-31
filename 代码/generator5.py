import random

#一个进行了异常处理的生成器函数：
def gen4():
    try:
        while True:
            n = random.random()
            yield n
    except RuntimeError:
        return 0
