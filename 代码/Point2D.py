class Point2D:
    #类属性dimension。
    dimension = 2

    #在初始化时设置了实例属性x和y。
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #类属性move。
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    #类属性location。
    def location(self):
        print("(" + str(self.x) + ", " + str(self.y) + ")")

