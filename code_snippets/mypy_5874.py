T = TypeVar('T')
S = TypeVar('S')

def add(x: List[T], y: List[S]) -> List[Union[T, S]]: ...

a: List[int]
b: List[str]

e: List[Union[int, str]] = add(a, b)
