class Planet(Enum):
    MERCURY = (3.303e+23, 2.4397e6)
    VENUS = (4.869e+24, 6.0518e6)

    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius

    @property
    def surface_gravity(self) -> float:
        G = 6.67300E-11
        return G * self.mass / (self.radius * self.radius)

def get_gravity(x: Planet) -> float:
    reveal_type(x)  # Revealed type is 'main.Planet'
    if x is Planet.MERCURY:
        reveal_type(x)  # Revealed type is 'Literal[main.Planet.MERCURY]'
        return 0.0

   # the alleged bug is in the line below, as I expected :Revealed type is 'Literal[main.Planet.VENUS]'
    reveal_type(x)  # Revealed type is 'Union[Literal[main.Planet.VENUS], Literal[main.Planet.mass], Literal[main.Planet.radius]]'
    return x.surface_gravity

class Planet(Enum):
    MERCURY = auto()
    VENUS = auto()


def get_gravity(x: Planet) -> float:
    reveal_type(x)  # Revealed type is 'main.Planet'
    if x is Planet.MERCURY:
        reveal_type(x)  # Revealed type is 'Literal[main.Planet.MERCURY]'
        return 0.0

    # here, the revealed type is as expected :
    reveal_type(x)  # Revealed type is 'Literal[main.Planet.VENUS]'
    return 1.0

