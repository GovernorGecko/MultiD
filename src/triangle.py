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

        # Position
        if (
            isinstance(positions, list) and len(positions) == 3 and
            all(type(p).__name__ == "Vector3" for p in positions)
        ):
            self.__positions = positions
        else:
            raise ValueError("Positions must be a List of Vector3s.")

        # Colors
        if colors is not None:
            if (
                isinstance(colors, list) and len(colors) == 3 and
                all(type(c).__name__ == "Vector3" for c in colors)
            ):
                self.__colors = colors
            else:
                raise ValueError("Colors must be a List of Vector3s.")
        else:
            self.__colors = None

        # TexCoords
        if texcoords is not None:
            if (
                isinstance(texcoords, list) and len(texcoords) == 3 and
                all(type(t).__name__ == "Vector2" for t in texcoords)
            ):
                self.__texcoords = texcoords
            else:
                raise ValueError("TexCoords must be a List of Vector2s.")
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
                [v + offset for v in self.__positions],
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

    def get_texcoords(self):
        """
        returns
            List<Vector2> texcoords
        """
        return self.__texcoords

    def get_vertex_data(
        self, positions=True, normals=True,
        colors=True, texcoords=True
    ):
        """
        parameters
            4 optional bools; positions, normals, colors, texcoords.
            These tell the getter to return these values or not.
        returns
            [[float x 6]] x 3 vertexes of this triangle.
        """
        vertex_data = []
        for i in range(0, 3):
            vertex = []
            if positions:
                vertex.extend(self.__positions[i].get_tuple())
            if normals:
                vertex.extend(self.__normals.get_tuple())
            if colors and self.__colors is not None:
                vertex.extend(self.__colors[i].get_tuple())
            if texcoords and self.__texcoords is not None:
                vertex.extend(self.__texcoords[i].get_tuple())
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

    def get_yaw(self, angle):
        """
        """

        # Angle okay?
        if not isinstance(angle, (float, int)):
            ValueError("Angle must be a float or int.")

        # Yaw Matrix
        yaw_matrix = Matrix(
            3, 3,
            [
                math.cos(angle), -math.sin(angle), 0.0,
                math.sin(angle), math.cos(angle), 0.0,
                0.0, 0.0, 1.0,
            ]
        )

        """
        yaw_triangle = Triangle(
            [
                [
                    (p.get_matrix() * yaw_matrix)
                ] for p in self.__positions
            ]
        )
        """

        for p in self.__positions:
            print(yaw_matrix * p.get_matrix())

        # for v in self.__positions:

        # print(yaw_triangle)
                
