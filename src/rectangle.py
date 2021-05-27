"""
Rectangle
"""

from .vector import Vector2


class Rectangle():
    """
    Parameters
    ----------
        Vector2
    """

    __slots__ = ["__bottom_right", "__top_left"]

    def __init__(
        self, top_left, bottom_right
    ):
        if (
            not all(
                isinstance(i, Vector3) for i in [
                    top_left, top_right, bottom_left, bottom_right
                ]
            )
        ):            
            raise ValueError("Corners ")

        self.__center = center

        self._bottom = bottom
        self._left = left
        self._right = right
        self._top = top

    def get(self):
        """
        Gets a tuple of our values.
        Returns
        -------
            Tuple(float, float, float, float)
        """
        return(self._left, self._right, self._bottom, self._top)

    def scaleHeight(self, scale):
        """
        Scales our height to the given value.
        Parameters
        ----------
            scale<float>
        Returns
        ------
            Tuple(float, float, float, float)
        """
        self._bottom *= scale
        self._top *= scale
        return self.get()

    def scaleWidth(self, scale):
        """
        Scales our width to the given value.
        Parameters
        ------
            scale<float>
        Returns
        ------
            Tuple(float, float, float, float)
        """
        self._left *= scale
        self._right *= scale
        return self.get()

    def setOffset(self, left, top):
        """
        Sets our left/top offset.
        Parameters
        ------
            left<float>
            top<float>
        Returns
        ------
            Tuple(float, float, float, float)
        """
        self._left = left
        self._top = top
        return self.get()
