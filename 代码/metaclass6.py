#定义元类。
class FixedAttrMeta(type):
    def __init__(self, *args, **kwargs):
        #从类定义语句中的attributes关键字获得类属性及其初始值。  将其记录到attrs
        # 属性中。
        self.attrs = kwargs["attributes"]
        #初始化所有类属性。
        for k, v in self.attrs.items():
            setattr(self, k, v)
        super().__init__(*args, **kwargs)

    #通过反射使得不能添加类属性，也不能修改attrs属性。
    def __setattr__(self, name, value):
        if name == "attrs":
            if not hasattr(self, "attrs"):
                super().__setattr__(name, value)
            else:
                raise Exception("Can not modify attribute attrs!")
        elif name in self.attrs:
            super().__setattr__(name, value)
        else:
            raise Exception(f"Can not add attribute {name}!")

    #通过反射使得不能删除类属性。
    def __delattr__(self, name):
        if name == "attrs" or name in self.attrs:
            raise Exception(f"Can not delete attribute {name}!")
        else:
            return None


#定义一个基类，使得__init_subclass__可以接受任何参数。
class FixedAttrBase():
    @classmethod
    def __init_subclass__(cls, *args, **kwargs):
        object.__init_subclass__()


#定义属于FixedAttrMeta的类A，它以FixedAttrBase为基类，除了attr外还具有x和y两个
# 类属性。
class A(FixedAttrBase, metaclass=FixedAttrMeta, attributes={"x": 0, "y":0}):
    pass



