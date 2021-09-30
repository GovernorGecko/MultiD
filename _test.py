"""
Testing MultiD features
"""

from src.shape import ShapeData, Shape
# from src.cube import Cube
# from src.matrix import Matrix
# from src.plane import Plane
# from src.triangle import Triangle
from src.vector import Vector3, Vector2, Vector4

p1 = Vector3(0.0, 0.0, 0.0)
p2 = Vector3(1.0, 1.0, 0.0)
p3 = Vector3(0.0, 1.0, 0.0)

c1 = Vector3(1.0, 0.0, 0.0)  # R
c2 = Vector3(0.0, 1.0, 0.0)  # G
c3 = Vector3(0.0, 0.0, 1.0)  # B

t1 = Vector2(0.0, 0.0)
t2 = Vector2(1.0, 0.0)
t3 = Vector2(0.0, 1.0)
t4 = Vector2(1.0, 1.0)

v4 = Vector4()
print(type(v4))


# s3d = Shape3D()

sd1 = ShapeData(
    [0, 1, 2],
    [p1, p2, p3]
)

sd2 = ShapeData(
    [0, 0, 0],
    [Vector3(0.0, 0.0, 0.0)]
)

s1 = Shape(sd1)

print(sd1 == sd2)

# import inspect
# print(inspect.getmro(type(sd1)))
# print(inspect.getmro(type(t1)))

"""
matrix = Matrix(3, 1, [4.0, 5.0, 6.0])

print(matrix.get_column_values(0))
print(matrix)
print(matrix.get_columns_length())
other_matrix = Matrix(1, 3)
other_matrix.set_value(0, 0, 1.0)
other_matrix.set_value(0, 1, 2.0)
other_matrix.set_value(0, 2, 3.0)
print(matrix * other_matrix)
"""

"""
p = Plane(
    colors=[c1, c2, c3, c1],
    texcoords=[t1, t2, t3, t4],
)

print(p)

print(
    p.get_triangles(
        offset=Vector3(1.0, 0.0, 0.0),
        yaw=1.0
    )
)

"""


"""

t = Triangle([p1, p2, p3], [c1, c2, c3], [t1, t2, t3])

print("testing a triangle")
print(t)
print(t.get_offset_by(Vector3([1.0, 1.0, 1.0])).get_rotation(90))
print(t.get_rotation(90))
print(t.get_vertex_data(offset=Vector3([1.0, 1.0, 1.0]), yaw=90))

"""

"""

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

c = Cube(
    scale=1.0,
    colors=color_data,
    texcoords=texcoord_data
)

print("testing a cube")
print(c)

"""
