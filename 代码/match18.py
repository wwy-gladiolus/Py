import math
from Point2DFixed import Point2DFixed


class Point(Point2DFixed):
    __match_args__ = ('x', 'y')


def get_distance(p1=None, p2=None):
    match p1, p2:
        case (None, None):
            print("No points.")
        case (Point(x1, y1), None):
            print("A single point, the distance from it to origin is "
                    + str(math.sqrt(x1**2 + y1**2)) + ".")
        case (Point(x1, y1), Point(x2, y2)):
            print("The distance between the two points is "
                    + str(math.sqrt((x1 - x2)**2 + (y1 - y2)**2)) + ".")

