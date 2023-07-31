#定义被用作装饰器的类。
class classname:
    def __init__(self, cls):
        if not hasattr(cls, 'classname'):
            def classname(self):
                return type(self).__name__
            classname.__qualname__ = cls.__qualname__ + '.classname'
            classname.__module__ = cls.__module__
            cls.classname = classname
        self.cls = cls
        self.__name__ = cls.__name__
        self.__qualname__ = cls.__qualname__
        self.__module__ = cls.__module__
        self.__doc__ = cls.__doc__
        self.__annotations__ = cls.__annotations__
        self.__bases__ = cls.__bases__
        self.__mro__ = cls.__mro__

    def __call__(self, *args, **kwargs):
        return self.cls(*args, **kwargs)


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


