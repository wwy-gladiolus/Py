from Point2DFixed import Point2DFixed

def match_point(p):
    match p:
        case Point2DFixed(x=0, y=0):
            print("This point is the origin.")
        case Point2DFixed(x=0):
            print("This point is on the y-axis.")
        case Point2DFixed(y=0):
            print("This point is on the x-axis.")
        case Point2DFixed(area=1):
            print("This point is on the unit circle.")
        case _:
            print("This point is not special.")
