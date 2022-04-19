from typing import Final

foo: Final[int | None] = 1

if foo is not None:
    def bar() -> None:
        reveal_type(foo) # note: Revealed type is "Union[builtins.int, None]"
