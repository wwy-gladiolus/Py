from random import randrange


class BranchAttr:
    #生成一个0～9之间的随机整数。
    n = randrange(0, 10)

    #当随机整数是0、1、2、3、4时定义star()属性。
    if n<5:
        def star():
            return '*'
    #当随机整数是5、6、7、8、9时定义dollar()属性。
    else:
        def dollar():
            return '$'

    #删除引用随机整数的标识符，避免它成为类的属性。
    del n

