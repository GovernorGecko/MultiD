"""
matrix.py
"""


class Matrix():
    """
    """

    __slots__ = ["__values"]

    def __init__(self, rows=1, columns=1):

        # Validate Columns and Rows
        if (
            not isinstance(columns, int) or
            not isinstance(rows, int) or
            columns <= 0 or
            rows <= 0
        ):
            ValueError("Columns and Rows must be ints > 0")

        # Build out our keys, with default values.
        self.__values = []
        for i in range(rows):
            self.__values.append([])
            for _ in range(columns):
                self.__values[i].append(0.0)

    def __str__(self):
        """
        """
        return str(self.__values)

    def __mul__(self, other):
        """
        """

        # Other a Matrix?
        if type(other).__name__ != "Matrix":
            ValueError(f"{type(other)} is not Matrix")
        # Our Columns same as other Rows?
        elif self.get_columns_length() != other.get_rows_length():
            ValueError("Expected our columns to equal other's rows.")

        # Create a new matrix, using our column length
        new_matrix = Matrix(
            self.get_rows_length(),
            other.get_columns_length(),
        )

        # Our Rows to Columns, multiplied by other Columns to Rows
        for i in range(self.get_rows_length()):
            for j in range(other.get_columns_length()):

                new_matrix.set_value(
                    i,
                    j,
                    self.dot(
                        self.__values[i],
                        other.get_column_values(j),
                    )
                )

        # Return the new Matrix!
        return new_matrix

    def dot(self, K, L):
        """
        """
        if len(K) != len(L):
            return 0

        return sum(i[0] * i[1] for i in zip(K, L))

    def get_columns_length(self):
        """
        """
        return len(self.__values[0])

    def get_column_values(self, column):
        """
        """

        # Valid Column
        if not self.is_valid_column(column):
            ValueError(f"{column} not valid for Matrix")

        # Return
        return [row[column] for row in self.__values]

    def get_rows_length(self):
        """
        """
        return len(self.__values)

    def get_value(self, row, column):
        """
        """

        # Valid Colunm/Row
        if (
            not self.is_valid_column(column) or
            not self.is_valid_row(row)
        ):
            ValueError(f"{column} or {row} not valid for Matrix")

        # Return!
        return self.__values[row][column]

    def is_valid_column(self, column):
        """
        """

        # Valid Column
        if (
            not isinstance(column, int) or
            column < 0 or self.get_columns_length() <= column
        ):
            return False
        return True

    def is_valid_row(self, row):

        # Valid Row
        if (
            not isinstance(row, int) or
            row < 0 or self.get_rows_length() <= row
        ):
            return False
        return True

    def set_value(self, row, column, value):
        """
        """

        # Valid Column/Row
        if (
            not self.is_valid_column(column) or
            not self.is_valid_row(row)
        ):
            ValueError(f"{column} or {row} not valid for Matrix")
        # Value must be a float
        elif not isinstance(value, float):
            ValueError("Value must be a float")

        # Set it
        self.__values[row][column] = value
