"""
Testing MultiD features
"""

# from src.cube import Cube
from src.square import Square
# from src.triangle import Triangle
from src.vector import Vector3, Vector2

p1 = Vector3(0.0, 0.0, 0.0)
p2 = Vector3(1.0, 1.0, 0.0)
p3 = Vector3(0.0, 1.0, 0.0)

c1 = Vector3(1.0, 0.0, 0.0)  # R
c2 = Vector3(0.0, 1.0, 0.0)  # G
c3 = Vector3(0.0, 0.0, 1.0)  # B

t1 = Vector2(0.0, 0.0)
t2 = Vector2(1.0, 0.0)
t3 = Vector2(1.0, 1.0)

s1 = Square(p1)

"""

t = Triangle([p1, p2, p3], [c1, c2, c3], [t1, t2, t3])

print("testing a triangle")
print(t)

color_data = [
    Vector3(1.0, 1.0, 1.0),
    Vector3(1.0, 1.0, 0.0),
    Vector3(1.0, 0.0, 0.0),
    Vector3(0.0, 0.0, 0.0),
    Vector3(0.0, 1.0, 0.0),
    Vector3(0.0, 1.0, 1.0),
    Vector3(0.0, 0.0, 1.0),
    Vector3(1.0, 0.0, 1.0),
]

texcoord_data = [
    Vector2(1.0, 1.0),
    Vector2(1.0, 0.0),
    Vector2(0.0, 0.0),
    Vector2(0.0, 1.0),
    Vector2(1.0, 1.0),
    Vector2(1.0, 0.0),
    Vector2(0.0, 0.0),
    Vector2(0.0, 1.0),
]

c = Cube(p1, colors=color_data, texcoords=texcoord_data)

print("testing a cube")
print(c)

"""
