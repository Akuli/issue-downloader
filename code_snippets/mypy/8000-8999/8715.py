import math
import typing

Tuple = typing.Tuple


def cartesian(r: int, θ: int) -> Tuple[float, float]:
    rad = math.radians(θ)
    return r*math.cos(rad), r*math.sin(rad)


r = 12
θ = 195

x,y = cartesian(r, θ)
print(f"({r}, {θ}°) = ({x:.2f}, {y:.2f})")

