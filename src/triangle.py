"""
OpenGL Triangle
This is the base for 3D.  It is made up of three Vertexes that
can contain up to four attributes each.
Position, required, a Vector3
Normal, calculated, a Vector3
TexCoord, optional, a Vector2
Color, optional, a Vector3
"""


import math

from .matrix import Matrix
from .vector import Vector3


class Triangle:
    """
    parameters
        list[Vector3]
            positions
        list[Vector3]
            colors
        list[Vector2]
            texcoords
    """

    __slots__ = ["__colors", "__normals", "__positions", "__texcoords"]

    def __init__(self, positions, colors=None, texcoords=None):

        print(positions)

        # Position
        if (
            isinstance(positions, list) and len(positions) == 3 and
            all(type(p).__name__ == "Vector" for p in positions)
        ):
            self.__positions = positions
        else:
            raise ValueError("Positions must be a List of Vectors.")

        # Colors
        if colors is not None:
            if (
                isinstance(colors, list) and len(colors) == 3 and
                all(type(c).__name__ == "Vector" for c in colors)
            ):
                self.__colors = colors
            else:
                raise ValueError("Colors must be a List of Vectors.")
        else:
            self.__colors = None

        # TexCoords
        if texcoords is not None:
            if (
                isinstance(texcoords, list) and len(texcoords) == 3 and
                all(type(t).__name__ == "Vector" for t in texcoords)
            ):
                self.__texcoords = texcoords
            else:
                raise ValueError("TexCoords must be a List of Vectors.")
        else:
            self.__texcoords = None

        # Calculate Normals
        """
        So for a triangle p1, p2, p3, if the vector U = p2 - p1
        and the vector V = p3 - p1 then the normal N = U X V and
        can be calculated by:
        Nx = UyVz - UzVy
        Ny = UzVx - UxVz
        Nz = UxVy - UyVx
        """
        position_U = self.__positions[1] - self.__positions[0]
        position_V = self.__positions[2] - self.__positions[0]
        self.__normals = Vector3(
            (position_U.Y * position_V.Z) - (position_U.Z * position_V.Y),
            (position_U.Z * position_V.X) - (position_U.X * position_V.Z),
            (position_U.X * position_V.Y) - (position_U.Y * position_V.X),
        )

    def __repr__(self):
        """
        returns
            __str__
        """
        return self.__str__()

    def __str__(self):
        """
        returns
            string representation of our triangle.
        """
        return str(self.get_vertex_data())

    def __eq__(self, other):
        """
        parameters
            Triangle
        returns
            bool of whether both triangles have the same vertexes.
        """
        if not type(other).__name__ == "Triangle":
            return False
        return all(other.has_position(p) for p in self.__positions)

    def __mul__(self, other):
        """
        parameters
            Matrix
        returns
            Triangle
        """
        # Multiplying against a Matrix.
        if type(other).__name__ == "Matrix":
            return Triangle(
                [
                    Vector3(
                        (other * p.get_matrix()).get_as_list()
                    ) for p in self.__positions
                ],
                self.__colors,
                self.__texcoords,
            )
        return self

    def get_colors(self):
        """
        returns
            List<Vector3> colors
        """
        return self.__colors

    def get_normals(self):
        """
        returns
            List<Vector3> normals
        """
        return self.__normals

    def get_offset_by(self, offset):
        """
        parameters
            Vector3
        returns
            Triangle
        """
        if type(offset).__name__ == "Vector3":
            return Triangle(
                [p + offset for p in self.__positions],
                self.__colors,
                self.__texcoords
            )
        return self

    def get_positions(self):
        """
        returns
            List<Vector3> positions
        """
        return self.__positions

    def get_rotation(self, yaw=0.0, pitch=0.0, roll=0.0):
        """
        parameters
            float
                yaw, or z
            float
                pitch, or y
            float
                roll, or z
        returns
            Triangle
        """

        if (
            not isinstance(yaw, (float, int)) or
            not isinstance(pitch, (float, int)) or
            not isinstance(roll, (float, int))
        ):
            ValueError("Yaw/Pitch/Roll must be a Float or Int")

        # Convert degrees to radians
        pitch_radians = math.radians(pitch)
        roll_radians = math.radians(roll)
        yaw_radians = math.radians(yaw)

        # Pitch, or Y
        pitch_matrix = Matrix(
            3, 3,
            [
                math.cos(pitch_radians), 0.0, math.sin(pitch_radians),
                0.0, 1.0, 0.0,
                -math.sin(pitch_radians), 0.0, math.cos(pitch_radians),
            ]
        )

        # Roll, or X
        roll_matrix = Matrix(
            3, 3,
            [
                1.0, 0.0, 0.0,
                0.0, math.cos(roll_radians), -math.sin(roll_radians),
                0.0, math.sin(roll_radians), math.cos(roll_radians),
            ]
        )

        # Yaw, or Z
        yaw_matrix = Matrix(
            3, 3,
            [
                math.cos(yaw_radians), -math.sin(yaw_radians), 0.0,
                math.sin(yaw_radians), math.cos(yaw_radians), 0.0,
                0.0, 0.0, 1.0,
            ]
        )

        # Order is Yaw * Pitch * Roll
        rotation_matrix = yaw_matrix * pitch_matrix * roll_matrix

        # Return a new Triangle
        return self * rotation_matrix

    def get_texcoords(self):
        """
        returns
            List<Vector2> texcoords
        """
        return self.__texcoords

    def get_transformed(
        self,
        offset=Vector3(0.0, 0.0, 0.0),
        yaw=0.0, pitch=0.0, roll=0.0,
    ):
        """
        parameters
            Vector3
                offset
            float
                yaw, or z
            float
                pitch, or y
            float
                roll, or x
        returns
            Triangle
        """
        return self.get_offset_by(
                offset
            ).get_rotation(
                yaw, pitch, roll
            )

    def get_vertex_data(
        self, positions=True, normals=True,
        colors=True, texcoords=True,
        offset=Vector3(0.0, 0.0, 0.0),
        yaw=0.0, pitch=0.0, roll=0.0
    ):
        """
        parameters
            4 optional bools; positions, normals, colors, texcoords.
                These tell the getter to return these values or not.
            Vector3
                offset
            float
                yaw, or z
            float
                pitch, or y
            float
                roll, or x
        returns
            [[float x 6]] x 3 vertexes of this triangle.
        """

        # Get a Transformed Triangle
        transformed_triangle = self.get_transformed(
            offset, yaw, pitch, roll
        )

        vertex_data = []
        for i in range(0, 3):
            vertex = []
            if positions:
                vertex.extend(
                    transformed_triangle.get_positions()[i].get_tuple()
                )
            if normals:
                vertex.extend(
                    transformed_triangle.get_normals().get_tuple()
                )
            if colors and self.__colors is not None:
                vertex.extend(
                    transformed_triangle.get_colors()[i].get_tuple()
                )
            if texcoords and self.__texcoords is not None:
                vertex.extend(
                    transformed_triangle.get_texcoords()[i].get_tuple()
                )
            vertex_data.append(vertex)
        return vertex_data
        """
        return [
            [*p.get_tuple(), *self.__normals.get_tuple()]
            for p in self.__positions
        ]
        """

    def has_position(self, position):
        """
        parameters
            Vector3
        returns
            bool of whether the given Vector3 matches one of ours.
        """
        if not type(position).__name__ == "Vector3":
            return False
        return position in self.__positions
