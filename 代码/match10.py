from Point2D import Point2D
from Point2DFixed import Point2DFixed


class Point(Point2DFixed):
    __match_args__ = ('x', 'y')


def match_point(p):
    match p:
        case Point2D(x=0, y=0):
            print("This Point2D point is the origin.")
        case Point2DFixed(x=0):
            print("This Point2DFixed point is on the y-axis.")
        case Point(_, 0):
            print("This Point point is on the x-axis.")
        case Point2D():
            print("This Point2D point is not special.")
        case Point2DFixed():
            print("This Point2DFixed point is not special.")
        case Point():
            print("This Point point is not special.")
