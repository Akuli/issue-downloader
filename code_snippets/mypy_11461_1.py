def get_gravity(x: Planet) -> float:
    reveal_type(x)  # Revealed type is 'main.Planet'
    if x is Planet.MERCURY:
        reveal_type(x)  # Revealed type is 'Literal[main.Planet.MERCURY]'
        return 0.0

   # the alleged bug is in the line below, as I expected :Revealed type is 'Literal[main.Planet.VENUS]'
    reveal_type(x)  # Revealed type is 'Union[Literal[main.Planet.VENUS], Literal[main.Planet.mass], Literal[main.Planet.radius]]'
    return x.surface_gravity
