_T = TypeVar('_T')
def noop_parser(x: str) -> str:
    return x

def foo(value: str, parser: Callable[[str], _T] = noop_parser) -> _T:
    return parser(value)
