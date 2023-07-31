import weakref

#定义两个将被弱引用的不可哈希对象。
st1 = {'a'}
st2 = {'b'}


#该函数显示WeakValueDictionary对象的值。
def show_values(wvd):
    #调用valuerefs()以获得所有ref对象。
    for wr in wvd.valuerefs():
        o = wr()
        if o is None:
            pass
        else:
            print(o)


#创建一个空的WeakValueDictionary对象。
wvd1 = weakref.WeakValueDictionary()

#将键值对插入wvd1。
wvd1[1] = st1
wvd1[2] = st2

#创建wvd1的拷贝。
wvd2 = weakref.WeakValueDictionary(wvd1)

#显示wvd1和wvd2的初始状态。
print("initially")
print("wvd1:")
show_values(wvd1)
print("wvd2:")
show_values(wvd2)
print("")

#删除st1，然后显示wvd1和wvd2现在的状态。
print("delete {st1}")
del st1
print("wvd1:")
show_values(wvd1)
print("wvd2:")
show_values(wvd2)
print("")

#删除st2，然后显示wvd1和wvd2现在的状态。
print("delete {st2}")
del st2
print("wvd1:")
show_values(wvd1)
print("wvd2:")
show_values(wvd2)
print("")

