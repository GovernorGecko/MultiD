"""
Cube
"""

from .triangle import Triangle
from .vector import Vector3


class Cube:
    """
        p1----p2
       /|*****/|
      p3----p4*|
      |*p5---|p6
      |/*****|/
      p7----p8
    """

    __slots__ = ["__triangles"]

    def __init__(
        self, center, colors=None, scale=1.0, texcoords=None
    ):
        self.__triangles = []

        # Base center should be a Vector3
        if not isinstance(center, Vector3):
            raise ValueError("Expected a Vector3 for the center.")

        # Scale.
        if not isinstance(scale, float) or scale < 0.0:
            scale = 1.0
        half_scale = scale * 0.5

        # Create our.. points
        p1 = Vector3(center.X - half_scale, center.Y + half_scale, center.Z - half_scale)
        p2 = Vector3(p1.X, p1.Y, p1.Z).offset(x=1.0)
        p3 = Vector3(p1.X, p1.Y, p1.Z).offset(z=1.0)
        p4 = Vector3(p1.X, p1.Y, p1.Z).offset(x=1.0, z=1.0)
        p5 = Vector3(p1.X, p1.Y, p1.Z).offset(y=-1.0)
        p6 = Vector3(p5.X, p5.Y, p5.Z).offset(x=1.0)
        p7 = Vector3(p5.X, p5.Y, p5.Z).offset(z=1.0)
        p8 = Vector3(p5.X, p5.Y, p5.Z).offset(x=1.0, z=1.0)

        # Top
        self.__triangles.append(Triangle([p2, p1, p3]))
        self.__triangles.append(Triangle([p3, p4, p2]))

        # Side X+
        self.__triangles.append(Triangle([p2, p4, p8]))
        self.__triangles.append(Triangle([p8, p6, p2]))

        # Side X=
        self.__triangles.append(Triangle([p3, p1, p5]))
        self.__triangles.append(Triangle([p5, p7, p3]))

        # Side Z+
        self.__triangles.append(Triangle([p4, p3, p7]))
        self.__triangles.append(Triangle([p7, p8, p4]))

        # Size Z=
        self.__triangles.append(Triangle([p1, p2, p6]))
        self.__triangles.append(Triangle([p6, p5, p1]))

        # Bottom
        self.__triangles.append(Triangle([p6, p5, p7]))
        self.__triangles.append(Triangle([p7, p8, p6]))
        
    def __str__(self):
        """
        Returns the Triangles that make up this Cube.
        """
        return str(self.__triangles)

    def get_triangles(self):
        """
        Returns:
            list[Triangle] the triangles that make up this cube.
        """
        return self.__triangles
