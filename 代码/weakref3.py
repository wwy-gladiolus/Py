import weakref

#定义两个将被弱引用的可哈希对象。
fs1 = frozenset({'a'})
fs2 = frozenset({'b'})


#该函数显示WeakKeyDictionary对象的键值对。
def show_kv_pairs(wkd):
    #调用keyrefs()以获得所有ref对象。
    for wr in wkd.keyrefs():
        o = wr()
        if o is None:
            pass
        else:
            print(f"{o}: {wkd[o]}")


#创建一个空的WeakKeyDictionary对象。
wkd1 = weakref.WeakKeyDictionary()

#将键值对插入wkd1。
wkd1[fs1] = 1
wkd1[fs2] = 2

#创建wkd1的拷贝。
wkd2 = weakref.WeakKeyDictionary(wkd1)

#显示wkd1和wkd2的初始状态。
print("initially")
print("wkd1:")
show_kv_pairs(wkd1)
print("wkd2:")
show_kv_pairs(wkd2)
print("")

#删除fs1，然后显示wkd1和wkd2现在的状态。
print("delete {fs1}")
del fs1
print("wkd1:")
show_kv_pairs(wkd1)
print("wkd2:")
show_kv_pairs(wkd2)
print("")

#删除fs2，然后显示wkd1和wkd2现在的状态。
print("delete {fs2}")
del fs2
print("wkd1:")
show_kv_pairs(wkd1)
print("wkd2:")
show_kv_pairs(wkd2)
print("")

