from Point2DFixed import Point2DFixed


class Point(Point2DFixed):
    __match_args__ = ('x', 'y')


def identify_shape(points):
    match points:
        case []:
            print("No points.")
        case [Point() as p1]:
            print("A single point at ("
                    + str(p1.x) + ", "
                    + str(p1.y) + ").")
        case [Point() as p1, Point() as p2]:
            print("A line segment from ("
                    + str(p1.x) + ", "
                    + str(p1.y) + ") to ("
                    + str(p2.x) + ", "
                    + str(p2.y) + ").")
        case [Point() as p1, *middle, Point() as p2]:
            print("A polygonal line segment from ("
                    + str(p1.x) + ", "
                    + str(p1.y) + ") to ("
                    + str(p2.x) + ", "
                    + str(p2.y) + ") with "
                    + str(len(middle)) + " middle points.")
