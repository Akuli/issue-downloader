from typing import Literal

class Some:
    def __init__(self) -> None:
        self.a = 1

s = Some()

reveal_type(s.a)  # Revealed type is "builtins.int"
reveal_type(getattr(s, 'a'))  # Revealed type is "Any"
reveal_type(getattr(s, 'b'))  # Revealed type is "Any"
reveal_type(getattr(s, 'a', None))  # Revealed type is "Union[Any, None]"

a: Literal['a']
reveal_type(getattr(s, a))  # Revealed type is "Any"

ab: Literal['a', 'b']
reveal_type(getattr(s, ab))  # Revealed type is "Any"

from typing import Literal

class Some:
    def __init__(self) -> None:
        self.a = 1

s = Some()

reveal_type(s.a)  # Revealed type is "builtins.int"
reveal_type(getattr(s, 'a'))  # Revealed type is "builtins.int"
reveal_type(getattr(s, 'b'))  # error: "Some" has no attribute "b"
reveal_type(getattr(s, 'a', None))  # Revealed type is "builtins.int"

a: Literal['a']
reveal_type(getattr(s, a))  # Revealed type is "builtins.int"

ab: Literal['a', 'b']
reveal_type(getattr(s, ab))  # error: "Some" has no attribute "b"
reveal_type(getattr(s, ab, None))  # Revealed type is "builtins.int | None"

