#定义被用作装饰器的函数。
def classname(cls):
    if not hasattr(cls, 'classname'):
        def classname(self):
            return type(self).__name__
        classname.__qualname__ = cls.__qualname__ + '.classname'
        classname.__module__ = cls.__module__
        cls.classname = classname
    return cls


#定义被装饰的目标类A。
@classname
class A:
    pass


#定义被装饰的目标B。
@classname
class B:
    pass


#定义被装饰的目标C。
@classname
class C:
    def classname(self):
        return 'Class Name: C'


