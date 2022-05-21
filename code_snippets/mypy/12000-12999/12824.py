from typing import NewType

Euro = NewType("Euro", float)

def to_eur(user_in: int | float | str) -> Euro:
    reveal_type(user_in) # int | float | str as expected
    if isinstance(user_in, float):
        reveal_type(user_in) # float
        return Euro(user_in)
    reveal_type(user_in) # str, but expected str | int
    converted = float(user_in.rstrip("€"))
    return Euro(converted)
    

print(to_eur(10))  # Raises type error as int has no method rstrip

from typing import NewType

Euro = NewType("Euro", float)

def to_eur(user_in: float | str) -> Euro:
    reveal_type(user_in) # float | str as expected
    if isinstance(user_in, float):
        reveal_type(user_in) # float
        return Euro(user_in)
    reveal_type(user_in) # str
    converted = float(user_in.rstrip("€"))
    return Euro(converted)
    

print(to_eur(10))   # Raises type error as int has no method rstrip
