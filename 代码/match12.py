from Point2D import Point2D
from Point2DFixed import Point2DFixed

def match_point(p):
    match p:
        case Point2D(x=0, y=0) | Point2DFixed(x=0, y=0) :
            print("This point is the origin.")
        case Point2D(x=0) | Point2DFixed(x=0) :
            print("This point is on the y-axis.")
        case Point2D(y=0) | Point2DFixed(y=0):
            print("This point is on the x-axis.")
        case Point2D() | Point2DFixed():
            print("This Point point is not special.")
