"""
Cube
"""

from .triangle import Triangle
from .vector import Vector3


class Cube:
    """
    parameters
        Vector3
            center of the cube
        (optional)
        list[Vector3]
            List of colors, starting at p1 and going to p8
        float
            Scale for Cube size
        list[Vector2]
            List of Texcoords, starting at p1 and goign to p8

        p1----p2
       /|*****/|
      p3----p4*|
      |*p5---|p6
      |/*****|/
      p7----p8
    """

    __slots__ = ["__triangles"]

    def __init__(
        self, center,
        colors=None, scale=1.0, texcoords=None
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

        # TexCoords must be 8 Vector2s
        if texcoords is not None:
            if (
                not isinstance(texcoords, list) or len(texcoords) != 8 or
                not all(type(t).__name__ == "Vector2" for t in texcoords)
            ):
                raise ValueError("TexCoords must be a List of Vector2s.")

        # Sequence of points
        sequence_of_points = [
            # top
            1, 0, 2,
            2, 3, 1,
            # side x+
            1, 3, 7,
            7, 5, 1,
            # side x-
            2, 0, 4,
            4, 6, 2,
            # side z+
            3, 2, 6,
            6, 7, 3,
            # side z-
            0, 1, 5,
            5, 4, 0,
            # bottom
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
            current_sequence_indexes = sequence_of_points[i:i + 3]
            self.__triangles.append(
                Triangle(
                    self.__get_list_values_from_indexes(
                        points,
                        current_sequence_indexes,
                    ),
                    self.__get_list_values_from_indexes(
                        colors,
                        current_sequence_indexes,
                    ),
                    self.__get_list_values_from_indexes(
                        texcoords,
                        current_sequence_indexes,
                    )
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

    def __get_list_values_from_indexes(self, list_data, indexes):
        """
        Assumes indexes exist in list.
        parameters
            list[var]
            list[int]
        returns
            None or list[var]
        """
        if list_data is not None:
            return [list_data[i] for i in indexes]
        return None

    def get_triangles(self):
        """
        returns
            list[Triangle]
                Triangles that make up this cube.
        """
        return self.__triangles
