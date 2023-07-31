def outer():
    #定义一个用于储存闭包的列表。
    inner = list()
    n = 3
    while n > 0:
        #循环三次，每次都产生一个返回自由变量n的闭包。
        def f():
            return n
        inner.append(f)
        n = n-1
    return inner

