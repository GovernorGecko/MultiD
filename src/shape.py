"""
Shape
"""

from .triangle import Triangle
from .vector import Vector3


class ShapeData():
    """
    required
        list[Vector]
            This list can coincide with a given sequence, if it doesn't
            it'll be built out with one.
    optional
        list[Int]
            Sequence of Vectors
        int
            How many vectors per
    """

    __slots__ = ["__sequence", "__vectors"]

    def __init__(self, vectors, sequence=None):

        # We require a list of vectors at least
        if (
            not isinstance(vectors, list) or
            not all(type(v).__name__ == "Vector" for v in vectors)
        ):
            raise ValueError("Vectors must b e a list of Vectors.")
        # If we did pass a sequence, need to make sure it is valid.
        elif sequence is not None:
            if (
                not isinstance(sequence, list) or
                not all(isinstance(s, int) for s in sequence) or
                len(sequence) % 3 != 0
            ):
                raise ValueError(
                    "Sequence must be a list of ints, "
                    "divisible by 3"
                )
            elif not all(s in range(len(vectors)) for s in sequence):
                raise ValueError(
                    "Sequence values must be within vectors range."
                )

        # Build a sequence!
        if sequence is None:
            self.__sequence = []
            self.__vectors = []
            for v in vectors:
                if v not in self.__vectors:
                    self.__sequence.append(
                        len(self.__vectors)
                    )
                    self.__vectors.append(v)
                else:
                    self.__sequence.append(
                        self.__vectors.index(
                            v
                        )
                    )
        # Just store the vals!
        else:
            self.__sequence = sequence
            self.__vectors = vectors

    def __eq__(self, other):
        """
        """
        if type(other).__name__ == type(self).__name__:
            return len(other.get_sequence()) == len(self.get_sequence())
        return False

    def __str__(self):
        """
        """
        return f"{self.__sequence} {self.__vectors}"

    def get_sequence(self):
        """
        """
        return self.__sequence

    def get_triangle_count(self):
        """
        """
        return len(self.__sequence) / 3

    def get_triangle_data(self, i):
        """
        """
        if i < self.get_triangle_count() and i >= 0:
            sequence_offset = i * 3
            return [
                self.get_vector_at(
                    sequence_offset
                ),
                self.get_vector_at(
                    sequence_offset + 1
                ),
                self.get_vector_at(
                    sequence_offset + 2
                ),
            ]
        return []

    def get_vectors(self):
        """
        """
        return self.__vectors

    def get_vector_at(self, i):
        """
        """
        return self.__vectors[
            self.__sequence[
                i
            ]
        ]


class Shape():
    """
    """

    __slots__ = ["__triangles"]

    def __init__(
        self,
        sequence,
        positions,
        colors=None,
        texcoords=None
    ):

        # Type Validation
        if (
            not isinstance(sequence, list) or
            not all(isinstance(s, int) for s in sequence)
        ):
            raise ValueError("Sequence must be a list of ints.")
        elif(
            not isinstance(positions, list) or
            not all(
                type(p).__name__ == "Vector" for p in positions
            )
        ):
            raise ValueError("Positions must be Vectors")
        elif(
            colors is not None and (
                not isinstance(colors, list) or
                not all(
                    type(c).__name__ == "Vector" for c in colors
                )
            )
        ):
            raise ValueError("Colors must be Vectors")
        elif(
            texcoords is not None and (
                not isinstance(texcoords, list) or
                not all(
                    type(t).__name__ == "Vector" for t in texcoords
                )
            )
        ):
            raise ValueError("Texcoords must be Vectors")

        # Create the ShapeData
        position_data = ShapeData(positions, sequence)

        color_data = None
        if colors is not None:
            color_data = ShapeData(colors, sequence)

        texcoord_data = None
        if texcoords is not None:
            texcoord_data = ShapeData(texcoords, sequence)

        # Iterate our Triangles in
        self.__triangles = []
        for i in range(int(position_data.get_triangle_count())):
            self.__triangles.append(
                Triangle(
                    self.__get_shape_data_from_index(position_data, i),
                    self.__get_shape_data_from_index(color_data, i),
                    self.__get_shape_data_from_index(texcoord_data, i)
                )
            )

    def __str__(self):
        """
        """
        return str(self.__triangles)

    def __get_shape_data_from_index(self, shape_data, i):
        """
        Assumes indexes exist in list.
        parameters
            ShapeData
            int
        returns
            None or list[var]
        """
        if shape_data is not None:
            return shape_data.get_triangle_data(i)
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
            t.get_transformed(
                offset=offset, yaw=yaw,
                pitch=pitch, roll=roll,
            ) for t in self.__triangles
        ]
