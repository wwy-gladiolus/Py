#通过标准输入获得一个正整数。
n = input("请输入一个正整数：")
n = int(n)
if n < 1:
    n = 1


class LoopAttr:
    #将n声明为全局变量，以避免它成为类的属性。
    global n

    #创建属性a1、a2、...、an。
    #分别将它们赋值1、2、...、n。
    while n > 0:
        exec('a'+str(n)+' = '+str(n))
        n = n-1

