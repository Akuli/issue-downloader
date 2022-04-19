import typing as t

T = t.TypeVar('T')
R = t.TypeVar('R')
Collector = t.Callable[[t.Iterable[T]], R]

def collect(it: t.Iterable[T], collector: Collector[T, R]) -> R:
  return collector(it)

collect(['str'], sorted)  # Argument 2 to "collect" has incompatible type overloaded function; expected "Callable[[Iterable[str]], List[SupportsLessThanT]]"
collect(['str'], set)     # Argument 2 to "collect" has incompatible type "Type[Set[Any]]"; expected "Callable[[Iterable[str]], Set[_T]]"
collect(['str'], list)    # Argument 2 to "collect" has incompatible type "Type[List[Any]]"; expected "Callable[[Iterable[str]], List[_T]]"

collect(['str'], lambda x: sorted(x))
collect(['str'], lambda x: set(x))
collect(['str'], lambda x: list(x))

