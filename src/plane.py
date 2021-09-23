"""
plane.py

A Plane in 3D Space, centered on Origin (0, 0, 0)
and spanning the X and Z axis.

"""

from .triangle import Triangle
from .vector import Vector3


class Plane():
    """
    p1----p2
    |      |
    |      |
    p3----p4

    parameters
        float
        list[Vector2 x 4]
        list[Vector3 x 4]
    """

    __slots__ = ["__triangles"]

    def __init__(
        self, scale=1.0, colors=None, texcoords=None
    ):

        # Scale should be a float
        if not isinstance(scale, float):
            raise ValueError("Expected a float for the scale")
        # Colors checker!
        elif (
            colors is not None and
            (
                not isinstance(colors, list) or
                (
                    isinstance(colors, list) and
                    (
                        len(colors) != 4 or
                        not all(
                            type(c).__name__ == "Vector3" for c in colors
                        )
                    )
                )
            )
        ):
            raise ValueError("Expected a List of 4 Vector2s for TexCoords")
        # Texcoords checker!
        elif (
            texcoords is not None and
            (
                not isinstance(texcoords, list) or
                (
                    isinstance(texcoords, list) and
                    (
                        len(texcoords) != 4 or
                        not all(
                            type(t).__name__ == "Vector2" for t in texcoords
                        )
                    )
                )
            )
        ):
            raise ValueError("Expected a List of 4 Vector2s for TexCoords")

        # Sequence of points
        sequence_of_points = [
            1, 0, 2,
            2, 3, 1,
        ]

        # Half the size to build out first point
        half_scale = scale / 2

        # Create our points.
        points = []
        points.append(
            Vector3(
                -half_scale,
                0.0,
                -half_scale
            )
        )
        points.append(Vector3(points[0]).offset(x=scale))
        points.append(Vector3(points[0]).offset(z=scale))
        points.append(Vector3(points[0]).offset(x=scale, z=scale))

        # Triangles
        self.__triangles = []

        # Iterate our sequence of points
        for i in range(0, len(sequence_of_points), 3):
            current_sequence_indexes = sequence_of_points[i:i + 3]
            self.__triangles.append(
                Triangle(
                    self.__get_list_values_from_indexes(
                        points,
                        current_sequence_indexes,
                    ),
                    colors=self.__get_list_values_from_indexes(
                        colors,
                        current_sequence_indexes,
                    ),
                    texcoords=self.__get_list_values_from_indexes(
                        texcoords,
                        current_sequence_indexes,
                    )
                )
            )

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

    def get_triangles(
        self, offset=Vector3(0.0, 0.0, 0.0),
        yaw=0.0, pitch=0.0, roll=0.0
    ):
        """
        parameters
            Vector3
            float
            float
            float
        returns
            Vector3
        """
        return [
            t.get_vertex_data(
                offset=offset, yaw=yaw,
                pitch=pitch, roll=roll
            ) for t in self.__triangles
        ]
