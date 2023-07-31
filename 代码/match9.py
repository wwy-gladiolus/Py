from Point2DFixed import Point2DFixed


class Point(Point2DFixed):
    __match_args__ = ('x', 'y')


def match_point(p):
    match p:
        case Point(0, 0):
            print("This point is the origin.")
        case Point(0):
            print("This point is on the y-axis.")
        case Point(_, 0):
            print("This point is on the x-axis.")
        case Point(_, _, area=1):
            print("This point is on the unit circle.")
        case _:
            print("This point is not special.")
