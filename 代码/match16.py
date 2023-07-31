from Point2DFixed import Point2DFixed


class Point(Point2DFixed):
    __match_args__ = ('x', 'y')


def identify_shape(points):
    match points:
        case []:
            print("No points.")
        case [Point()]:
            print("A single point.")
        case [Point(), Point()]:
            print("A line segment.")
        case [Point(), Point(), Point()]:
            print("A triangle.")
        case [Point(), Point(), *_, Point(), Point()]:
            print("A polygon.")
