#定义将作为Point2D类的__init__方法的函数。
def f1(self, x, y):
    self.x = x
    self.y = y


#定义将作为Point2D类的move方法的函数。
def f2(self, dx, dy):
    self.x += dx
    self.y += dy


#定义将作为Point2D类的location方法的函数。
def f3(self):
    print("(" + str(self.x) + ", " + str(self.y) + ")")


#定义Point2D类。
Point2D = type('Point2D', (), {
    'dimension': 2,
    '__init__': f1,
    'move': f2,
    'location': f3})


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

