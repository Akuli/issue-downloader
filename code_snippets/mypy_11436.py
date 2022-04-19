def foo() -> list[int] | list[None]:
    ...


bar = foo()

if bar[0] is not None:
    reveal_type(bar) # Revealed type is "Union[builtins.list[builtins.int], builtins.list[None]]
