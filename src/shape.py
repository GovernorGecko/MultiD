"""
Shape
"""

from .triangle import Triangle


class ShapeData():
    """
    """

    __slots__ = [
        "__iteration", "__sequence",
        "__vectors", "__vectors_per_sequence"
    ]

    def __init__(self, sequence, vectors, vectors_per_sequence=3):

        # Type validation
        if (
            not isinstance(sequence, list) or
            not all(isinstance(s, int) for s in sequence) or
            len(sequence) % vectors_per_sequence != 0
        ):
            raise ValueError(
                f"Sequence must be a list of ints, "
                f"divisible by {vectors_per_sequence}."
            )
        elif(
            not isinstance(vectors, list) or
            not all(type(v).__name__ == "Vector" for v in vectors)
        ):
            raise ValueError("Values must be of type Vector.")
        elif not all(s in range(len(vectors)) for s in sequence):
            raise ValueError("Sequence values must be within vectors range.")

        # Store
        self.__sequence = sequence
        self.__vectors = vectors
        self.__vectors_per_sequence = vectors_per_sequence

    def __eq__(self, other):
        """
        """
        if type(other).__name__ == type(self).__name__:
            return len(other.get_sequence()) == len(self.get_sequence())
        return False

    def __iter__(self):
        self.__iteration = 0
        return self

    def __next__(self):
        if(self.__iteration >= self.get_triangle_count()):
            raise StopIteration
        result = self.get_triangle_data(self.__iteration)
        self.__iteration += 1
        return result

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
        return len(self.__sequence) / self.__vectors_per_sequence

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
        position_data,
        color_data=None,
        texcoord_data=None
    ):

        # Type Validation
        if (
            not type(position_data).__name__ == "ShapeData" or
            (
                color_data is not None and
                (
                    not type(color_data).__name__ == "ShapeData" or
                    color_data != position_data
                )
            ) or
            (
                texcoord_data is not None and
                (
                    not type(texcoord_data).__name__ == "ShapeData" or
                    texcoord_data != position_data
                )
            )
        ):
            raise ValueError("Data must be of type ShapeData")

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

        print(self.__triangles)

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
