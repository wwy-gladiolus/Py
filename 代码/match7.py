from Point2D import Point2D
from Point2DFixed import Point2DFixed

def match_point(p):
    match p:
        case Point2D():
            print("This is a Point2D point.")
        case Point2DFixed():
            print("This is a Point2DFixed point.")
