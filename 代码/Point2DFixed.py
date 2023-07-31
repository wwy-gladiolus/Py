class Point2DFixed:
    dimension = 2
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def location(self):
        print("(" + str(self.x) + "," + str(self.y) + ")")

    #通过__slots__指定实例属性。
    __slots__ = ("x", "y", "area")

