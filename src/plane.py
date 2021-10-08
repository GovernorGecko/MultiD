"""
plane.py

A Plane in 3D Space, centered on Origin (0, 0, 0)
and spanning the X and Z axis.

"""

from .shape import Shape
from .vector import Vector3


def Plane(scale=1.0, colors=None, texcoords=None):
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

    # Scale should be a float
    if not isinstance(scale, float):
        raise ValueError("Expected a float for the scale")

    # Sequence of points
    sequence = [
        1, 0, 2,
        2, 3, 1,
    ]

    # Half the size to build out first point
    half_scale = scale / 2

    # Point1
    p1 = Vector3(
            -half_scale,
            0.0,
            -half_scale
        )

    # Create our points.
    points = []
    points.append(p1)
    points.append(p1 + Vector3(x=scale))
    points.append(p1 + Vector3(z=scale))
    points.append(p1 + Vector3(x=scale, z=scale))

    # Shape
    return Shape(
        sequence,
        points,
        colors,
        texcoords
    )
