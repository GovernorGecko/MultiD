"""
Cube
"""

from .shape import Shape
from .vector import Vector3


def Cube(scale=1.0, colors=None, texcoords=None):
    """
    parameters
        Vector3
            center of the cube
        (optional)
        list[Vector3]
            List of colors, starting at p1 and going to p8
        float
            Scale for Cube size
        list[Vector2]
            List of Texcoords, starting at p1 and goign to p8

        p1----p2
       /|     /|
      p3----p4 |
      | p5---|p6
      |/     |/
      p7----p8
    """

    # Scale should be a float
    if not isinstance(scale, float):
        raise ValueError("Expected a float for the scale")

    # Sequence of points
    sequence = [
        # top
        1, 0, 2,
        2, 3, 1,
        # side x+
        1, 3, 7,
        7, 5, 1,
        # side x-
        2, 0, 4,
        4, 6, 2,
        # side z+
        3, 2, 6,
        6, 7, 3,
        # side z-
        0, 1, 5,
        5, 4, 0,
        # bottom
        5, 4, 6,
        6, 7, 5,
    ]

    # Half Scale
    half_scale = scale * 0.5

    # Create our.. points
    points = []
    points.append(
        Vector3(
            -half_scale,
            half_scale,
            -half_scale,
        )
    )
    points.append(points[0] + Vector3(x=scale))
    points.append(points[0] + Vector3(z=scale))
    points.append(points[0] + Vector3(x=scale, z=scale))
    points.append(points[0] + Vector3(y=-scale))
    points.append(points[4] + Vector3(x=scale))
    points.append(points[4] + Vector3(z=scale))
    points.append(points[4] + Vector3(x=scale, z=scale))

    # Shape
    return Shape(
        sequence,
        points,
        colors,
        texcoords,
    )
