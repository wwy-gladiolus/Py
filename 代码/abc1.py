import abc


#定义类A。
class A:
    #该方法会成为继承A的抽象基类的混入方法。
    def a_mixin(self):
        print("a_mixin")


#定义抽象基类B。
class B(metaclass=abc.ABCMeta):
    #该方法是B的抽象方法。
    @abc.abstractmethod
    def b(self):
        print("b")


#定义抽象基类C。
class C(abc.ABC):
    #该类方法是C的抽象方法。
    @classmethod
    @abc.abstractmethod
    def c(cls):
        print("c")

    #该方法是C的混入方法。
    def c_mixin(self):
        print("c_mixin")


#定义抽象基类D。  它继承了类A，因此还具有混入方法a_mixin()。
class D(A, metaclass=abc.ABCMeta):
    #该静态方法是D的抽象方法。
    @staticmethod
    @abc.abstractmethod
    def d():
        print("d")


#定义抽象基类E。  它继承了抽象基类B，因此还具有抽象方法b()。  它也继承了抽象基类C，
# 因此还具有抽象方法c()和混入方法c_mixin()。
class E(B, C):
    #该方法是E的混入方法。
    def e_mixin(self):
        print("e_mixin")


#定义类F，它继承了抽象基类D。
class F(D):
    #重写D的抽象方法d()。
    @staticmethod
    def d():
        print("F's implementation of d()")
        #通过super()调用D的d()。  这是通过super()访问基类的静态方法的例子。
        super(F, F).d()


#定义类G，它继承了抽象基类E。
class G(E):
    #重写B的抽象方法b()。
    def b(self):
        print("G's implementation of b()")
        #通过super()调用B的b()。  这是通过super()访问基类的方法的例子。
        super().b()

    #重写C的抽象方法c()。
    @classmethod
    def c(cls):
        print("G's implementation of c()")
        #通过super()调用C的c()。  这是通过super()访问基类的类方法的例子。
        super().c()


