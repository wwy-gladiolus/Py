import types


#定义将作为Point2D类的__init__属性的函数。
def f1(self, x, y):
    self.x = x
    self.y = y


#定义将作为Point2D类的move属性的函数。
def f2(self, dx, dy):
    self.x += dx
    self.y += dy


#定义将作为Point2D类的location属性的函数。
def f3(self):
    print("(" + str(self.x) + ", " + str(self.y) + ")")


#定义传入new_class()的exec_body参数的回调函数。
def eb(ns):
    ns['dimension'] = 2
    ns['__init__'] = f1
    ns['move'] = f2
    ns['location'] = f3


#定义Point2D类。
Point2D = types.new_class('Point2D', exec_body=eb)


#修改类所属的模块。
Point2D.__module__ = '__main__'

#修改函数属性的名字和限定名字。
Point2D.__init__.__name__ = '__init__'
Point2D.__init__.__qualname__ = 'Point2D.__init__'
Point2D.move.__name__ = 'move'
Point2D.move.__qualname__ = 'Point2D.move'
Point2D.location.__name__ = 'location'
Point2D.location.__qualname__ = 'Point2D.location'

#删除不再需要的标识符。
del f1
del f2
del f3
del eb

