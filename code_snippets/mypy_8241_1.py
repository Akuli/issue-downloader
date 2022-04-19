def g(a: str) -> str: ...

reveal_type(f(g))  # N: Revealed type is 'Set[Any]'

def h(a: str, b: int) -> str: ...

reveal_type(f(g))  # N: Revealed type is 'List[Any]'
