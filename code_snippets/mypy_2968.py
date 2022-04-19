from typing import Tuple
from math import hypot

Point = Tuple[float, ...]
Centroid = Point

def dist(p: Centroid, q: Point) -> float:
    px, py = p
    qx, qy = q
    return hypot(px - qx, py - qy)

print( dist('xyz', (3.5, 7.2)) )
