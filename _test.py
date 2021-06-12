"""
Testing MultiD features
"""

from src.triangle import Triangle
from src.vector import Vector3

p1 = Vector3(0.0, 0.0, 0.0)
p2 = Vector3(1.0, 1.0, 0.0)
p3 = Vector3(0.0, 1.0, 0.0)

t = Triangle([p1, p2, p3])

print(t)