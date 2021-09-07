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
        self, center, colors=None, scale=1.0, texcoords=[None]
    ):
        self.__triangles = []

        # Base center should be a Vector3
        if not type(center).__name__ == "Vector3":
            raise ValueError("Expected a Vector3 for the center.")

        # Scale.
        if not isinstance(scale, float) or scale < 0.0:
            scale = 1.0
        half_scale = scale * 0.5

        # Colors must be 8 Vector3s
        if colors is not None:
            if (
                not isinstance(colors, list) or len(colors) != 8 or
                not all(type(c).__name__ == "Vector3" for c in colors)
            ):
                raise ValueError("Colors must be a List of Vector3s.")
        else:
            colors = [None for i in range(12)]

        # Sequence of points
        sequence_of_points = [
            1, 0, 2,
            2, 3, 1,
            1, 3, 7,
            7, 5, 1,
            2, 0, 4,
            4, 6, 2,
            3, 2, 6,
            6, 7, 3,
            0, 1, 5,
            5, 4, 0,
            5, 4, 6,
            6, 7, 5,
        ]

        # Create our.. points
        points = []
        points.append(
            Vector3(center).offset(x=-half_scale, y=half_scale, z=-half_scale)
        )
        points.append(Vector3(points[0]).offset(x=1.0))
        points.append(Vector3(points[0]).offset(z=1.0))
        points.append(Vector3(points[0]).offset(x=1.0, z=1.0))
        points.append(Vector3(points[0]).offset(y=-1.0))
        points.append(Vector3(points[4]).offset(x=1.0))
        points.append(Vector3(points[4]).offset(z=1.0))
        points.append(Vector3(points[4]).offset(x=1.0, z=1.0))

        # Iterate our sequence of points
        for i in range(0, len(sequence_of_points), 3):
            self.__triangles.append(
                Triangle(
                    [
                        points[
                            sequence_of_points[i]
                        ],
                        points[
                            sequence_of_points[i + 1]
                        ],
                        points[
                            sequence_of_points[i + 2]
                        ]
                    ],
                )
            )

        """
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
        """

    def __str__(self):
        """
        returns
            string
                Triangles that make up this Cube.
        """
        return str(self.__triangles)

    def get_aabb(sslf):
        """
        """
        print("hi")

    def get_triangles(self):
        """
        returns
            list[Triangle]
                Triangles that make up this cube.
        """
        return self.__triangles
