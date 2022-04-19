from dataclasses import dataclass
from typing import NamedTuple

@dataclass
class One:
    bar: int

f: One
reveal_type(f.__match_args__)  # Revealed type is "Tuple[Literal['bar']]"

class Two(NamedTuple):
    baz: str

g: Two
reveal_type(g.__match_args__)  # Revealed type is "Tuple[Literal['baz']]"
