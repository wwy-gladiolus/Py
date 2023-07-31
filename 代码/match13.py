import math
from Point2DFixed import Point2DFixed


class Point(Point2DFixed):
    __match_args__ = ('x', 'y')


def match_point(p):
    match p:
        case Point(0, 0):
            print("This point is the origin.")
        case Point(0, y):
            print("This point is on the y-axis, distance from origin is " + str(abs(y)) + ".")
        case Point(x, 0):
            print("This point is on the x-axis, distance from origin is " + str(abs(x)) + ".")
        case Point(x, y) if abs(math.sqrt(x**2 + y**2) - 1.0) < 1e-100:
            print("This point is on the unit circle.")
        case _:
            print("This point is not special.")
