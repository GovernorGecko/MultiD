"""
Shape
"""

from .triangle import Triangle


class ShapeData():
    """
    """

    __slots__ = ["__sequence", "__vectors"]

    def __init__(self, sequence, vectors):

        # Type validation
        if (
            not isinstance(sequence, list) or
            not all(isinstance(s, int) for s in sequence) or
            len(sequence) % 3 != 0
        ):
            raise ValueError("Sequence must be a list of ints, divisible by 3.")
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

    def get_vectors(self):
        """
        """
        return self.__vectors


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
                not type(color_data).__name__ == "ShapeData"
            ) or
            (
                texcoord_data is not None and
                not type(texcoord_data).__name__ == "ShapeData"
            )
        ):
            raise ValueError("Data must be of type ShapeData")

        # Create Triangles
        # self.__color_data = color_data
        # self.__position_data = position_data
        # self.__texcoord_data = texcoord_data
        for p in position_data.get_vectors():
            print(p)
        t = Triangle(
            [
                p for p in position_data.get_vectors()
            ]
        )
        print(t)