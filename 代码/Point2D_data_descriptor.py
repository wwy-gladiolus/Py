#该类是一个数据描述器。
class Dimension:
    def __init__(self, value):
        self.value = int(value)

    def __get__(self, instance, owner=None):
        return self.value

    #仅当通过实例设置该描述器时会被调用。
    def __set__(self, instance, value):
        print("Instances cannot change the value of its class attributes.")
        return None

    #仅当通过实例删除该描述器时会被调用。
    def __delete__(self, instance):
        print("Instances cannot delete its class attributes.")
        return None


class Point2D:
    #该属性引用一个数据描述器。
    dimension = Dimension(2)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def location(self):
        print("(" + str(self.x) + ", " + str(self.y) + ")")

