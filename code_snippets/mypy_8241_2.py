def m(a: str, *b: int) -> str: ...

reveal_type(f(m))  # N: Revealed type is 'Set[Any]'

def n(a: str, **b: int) -> str: ...

reveal_type(f(n))  # N: Revealed type is 'Set[Any]'
