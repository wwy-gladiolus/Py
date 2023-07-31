class Area:
    #该类的实例只具有两个实例属性：长度和高度。
    def __init__(self, l, h):
        self.length = l
        self.height = h
    
    #添加了__getattr__使得访问该类的实例的任何其他属性时都返回面积，就好像面积是该类
    # 实例的默认属性值。
    def __getattr__(self, name):
        return self.length * self.height

