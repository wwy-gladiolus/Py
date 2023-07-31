a = 1
print('a = ' + str(a))


def f1():
    b = 2
    print('b = ' + str(b))

    def f2():
        c = 3
        print('c = ' + str(c))

        def f3():
            d = 4
            #将标识符b和c声明为本地变量中的自由变量。
            nonlocal b, c
            #将标识符a声明为全局变量。
            global a
            #直接写入f2()定义的本地变量c。
            c = -3
            #直接写入f1()定义的本地变量b。
            b = -2
            #直接写入全局变量a。
            a = -1
            print('\n')
            #列出f3()视角的所有本地变量名称。
            print('dir: ' + str(dir()))
            #显示f3()视角的所有本地变量状态。
            print('locals: ' + str(locals()))
            #显示f3()视角的所有全局变量状态。
            print('globals: ' + str(globals()))
            print('\n')

        f3()
        print('c = ' + str(c))

    f2()
    print('b = ' + str(b))

f1()
print('a = ' + str(a))


print('\n')
#列出所有全局变量名称。
print('dir: ' + str(dir()))
#显示所有全局变量状态。
print('locals: ' + str(locals()))
#显示所有全局变量状态。
print('globals: ' + str(globals()))
