"""
Rectangle
"""

from .vector3 import Vector3


class Rectangle():
    """
    Rectangle
    For simple Rectangle things.
    Parameters
    ----------
        Vector3 center of Rectangle
    """

    __slots__ = ["__center", "__height", "__width"]

    def __init__(
        self, center=Vector3(), height=1.0, width=1.0,
        colors=None, scale=1.0, texcoords=None
    ):
        if (
            not isinstance(width, float) or
            not isinstance(height, float)
        ):
            raise ValueError("Width/Height must be floats.")
        elif not isinstance(center, Vector3):
            raise ValueError("Center must be a Vector3")

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
