import typing


#所有类的基类。
class PointBase(): ...


#直接派生自PointBase。
class Point3D(PointBase): ...


#直接派生自PointBase。
class PointMove(PointBase): ...


#直接派生自PointBase。
class PointShow(PointBase): ...


#派生自Point3D。
class Point3DMove(Point3D): ...


#T代表Point3D和它的子类。
T = typing.Type[Point3D]


def create_point(cls: T): ...


if __name__ == "__main__":
    create_point(PointBase)    #报错。
    create_point(Point3D)
    create_point(PointMove)    #报错。
    create_point(PointShow)    #报错。
    create_point(Point3DMove)
