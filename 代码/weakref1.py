import typing
import weakref


#定义一个函数。
def f1():
    print("I am a function, my name is 'f1'.")


#定义一个类，它没有设置__slots__，因此具有__weakref__属性。
class C1():
    def __init__(self, who):
        self.who = who

    def m1(self):
        print(f"I am '{self.who}'.")

    @classmethod
    def m2(cls):
        print(f"My class is '{cls.__name__}'.")


#定义一个类，它设置了__slots__，但由于以C1为基类，所以也具有__weakref__属性。
class C2(C1):
    __slots__ = 'who'

    @staticmethod
    def m3():
        print(f"I am 'C2'.")


#定义一个类，它不具有__weakref__属性。
class C3():
    __slots__ = 'who'

