#自定义异常类，具有下列实例属性：
#  low: 合法范围的下限。
#  high: 合法范围的上限。
#  current: 合法范围之外的当前值。
class RangeError(Exception):
    def __init__(self, *args, low=0, high=100, current=-1):
        self.low = low
        self.high = high
        self.current = current
        super().__init__(*args)

    #重写魔术属性__str__。
    def __str__(self):
        extra = ('The legal range is ['
                + str(self.low) + ',' + str(self.high)
                + '], but the current value is '
                + str(self.current) + '. ')
        return extra + super().__str__()


#定义代表温度计的类。
class Thermometer():
    def __init__(self, temperature=0):
        if temperature < -20 or temperature > 50:
            e = RangeError('Out of range!', low=-20, high=50, current=temperature)
            e.add_note("Raise during initialization!")
            raise e
        self.temperature = temperature

    #改变温度计的温度。
    def change(self, delta):
        temperature = self.temperature + delta
        if temperature < -20 or temperature > 50:
            e = RangeError('Out of range!', low=-20, high=50, current=temperature)
            e.add_note("Raise during changing!")
            raise e
        self.temperature = temperature

    #以“-”、“0”、“+”和“@”绘制温度计读数。  四个“-”代表零下温度区域，十个“+”
    # 代表零上温度区域，“0”代表零度。  “@”代表当前温度，需要替换掉一个“-”、
    # “0”或“+”。
    def show(self):
        scale = '----0++++++++++'
        index = self.temperature//5 + 4
        marked_scale = scale[0:index] + '@' + scale[index+1:14]
        print(marked_scale)

