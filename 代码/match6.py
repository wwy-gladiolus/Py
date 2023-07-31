class PrimaryColor:
    def __init__(self):
        self.red = 'red'
        self.green = 'green'
        self.blue = 'blue'


pri_co = PrimaryColor()


def pure_color(value):
    match value:
        case pri_co.red:
            print("This color is purely red.")
        case pri_co.green: 
            print("This color is purely green.")
        case pri_co.blue:
            print("This color is purely blue.")
        case _:
            print("This color is mixed.")

