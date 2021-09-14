"""
square.py

A Square in 3D Space

"""

from .vector import Vector3, Vector2


class Square():
    """

    p1----p2
    |      |
    |      |
    p3----p4

    parameters
        Vector3
        Vector2
            size of x/z, flat y
        Vector2
        Vector2
        list[Vector3]
        float
        float
        float
        
    Yaw, Pitch, Roll
    """

    __slots__ = ["__triangles"]

    def __init__(
        self, center, size=Vector2(1.0, 1.0),
        texcoords_center=None, texcoords_size=Vector2(1.0, 1.0),
        colors=None, yaw=0.0, pitch=0.0, roll=0.0
    ):

        # Base center should be a Vector3
        if not type(center).__name__ == "Vector3":
            raise ValueError("Expected a Vector3 for the center.")
        # Size should be a Vector2
        elif not type(size).__name__ == "Vector2":
            raise ValueError("Expected a Vector2 for the size")

        # Half the size to build out first point
        half_size = size / 2

        # Create our points.
        points = []
        points.append(
            Vector3(center).offset(
                x=-half_size.X,
                y=center.Y,
                z=-half_size.Y
            )
        )
        points.append(Vector3(points[0]).offset(x=1.0))
        points.append(Vector3(points[0]).offset(z=1.0))
        points.append(Vector3(points[0]).offset(x=1.0, z=1.0))

        print(points)
