"""
matrix.py
"""


class Matrix():
    """
    """

    def __init__(self, columns=1, rows=1):
        
        # Validate Columns and Rows
        if (
            not isinstance(columns, int) or
            not isinstance(rows, int) or
            columns <= 0 or
            rows <= 0
        ):
            ValueError("Columns and Rows must be ints > 0")

        


