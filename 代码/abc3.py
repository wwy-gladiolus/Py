import collections.abc


#定义继承Sequence的抽象基类。
class MySequence(collections.abc.Sequence):
    #重写__subclasshook__。
    @classmethod
    def __subclasshook__(cls, subclass):
        #仅当通过MySequence调用该属性时才需要做判断，通过MySequence的子类调用该
        # 属性时将直接返回NotImplemented。
        if cls is MySequence:
            #Sequence的虚子类必须是Collection的虚子类。
            if not issubclass(subclass, collections.abc.Collection):
                return False
            #Sequence的虚子类必须是Iterable的虚子类。
            if not issubclass(subclass, collections.abc.Iterable):
                return False
            #Sequence的虚子类还必须实现__reversed__、__getitem__、index()和
            # count()。
            if hasattr(subclass, "__reversed__") and\
                    hasattr(subclass, "__getitem__") and\
                    hasattr(subclass, "index") and\
                    hasattr(subclass, "count"):
                return True
        #无法通过上面的条件判断时，继续__subclasscheck__的后续步骤。
        return NotImplemented


