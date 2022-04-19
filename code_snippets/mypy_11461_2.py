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
