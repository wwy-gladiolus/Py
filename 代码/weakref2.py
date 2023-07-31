import weakref, sys

#定义第一个回调函数。
def cb1(wr):
    print("cb1 is called!")
    del wr
    raise RuntimeError()


#定义第二个回调函数。
def cb2(wr):
    print(f"cb2 is called!")
    del wr


#定义第三个回调函数。
def cb3(wr):
    print(f"cb3 is called!")
    del wr


#定义一个函数来显示一个对象的的引用数、弱引用数和ref对象。
def ref_stat(obj):
    print("Reference number: " + str(sys.getrefcount(obj)))
    print("WeakRef number: " + str(weakref.getweakrefcount(obj)))
    print("WeakRefs: " + repr(weakref.getweakrefs(obj)))
    print("")


if __name__ == "__main__":
    #创建两个集合。
    st1 = {'a', 'b', 'c'}
    st2 = {'c', 'b', 'a'}
    print(f"st1 is {st1}")
    print(f"st2 is {st2}")
    print("")

    #为st1创建第一个弱引用：
    wr1 = weakref.ref(st1, cb1)
    print("wr1's callback: " + repr(wr1.__callback__))
    ref_stat(st1)

    #为st1创建第二个弱引用：
    wr2 = weakref.ref(st1, cb2)
    print("wr2's callback: " + repr(wr2.__callback__))
    ref_stat(st1)

    #为st1创建第三个弱引用：
    wr3 = weakref.ref(st1, cb3)
    print("wr3's callback: " + repr(wr3.__callback__))
    ref_stat(st1)

    #为st2创建一个弱引用：
    wr4 = weakref.ref(st2)
    print("wr4's callback: " + repr(wr4.__callback__))
    print("")


    #验证弱引用之间的比较：
    print("wr1 == wr2 == wr3: " + str(wr1 == wr2 == wr3))
    print("wr1 == wr4: " + str(wr1 == wr4))
    print("delete st2!")
    del st2
    print("wr1 == wr4: " + str(wr1 == wr4))
    print("")

    #删除st1的第二个弱引用，然后删除st1本身。
    print("delete wr2!")
    del wr2
    ref_stat(st1)
    print("delete st1!")
    del st1

