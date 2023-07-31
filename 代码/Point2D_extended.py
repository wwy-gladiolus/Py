class Point2D:
    dimension = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def location(self):
        print("(" + str(self.x) + ", " + str(self.y) + ")")

    #该类方法将非函数类属性dimension重置为默认值。
    @classmethod
    def reset(cls):
        cls.dimension = 2

    #该静态方法输出一段说明文本，并以给定的符号做装饰。
    @staticmethod
    def declare(char='*'):
        n = 17
        line1 = ''
        while n > 0:
            line1 = line1 + char
            n = n - 1
        line2 = char+'               '+char
        print(line1)
        print(line2)            
        print(char+' class Point2D '+char)
        print(line2)
        print(line1)
