from hypothesis import strategies as st

st.lists(st.integers()).map(sorted)
# error: Argument to "map" of "SearchStrategy" has incompatible type overloaded function;
#        expected "Callable[[List[int]], List[SupportsRichComparisonT]]"

from typing import Callable, Generic, TypeVar
Ex = TypeVar("Ex")
T = TypeVar("T")

class Strategy(Generic[Ex]):
    def __init__(self, example: Ex) -> None:
        self.example = example

    def map(self, transform: Callable[[Ex], T]) -> "Strategy[T]":
        return Strategy(transform(self.example))

def lists(elements: Strategy[Ex]) -> Strategy[list[Ex]]:
    return Strategy([elements.example, elements.example])

s = lists(Strategy(0)).map(sorted)
# error: Argument to "map" of "Strategy" has incompatible type overloaded function;
#        expected "Callable[[List[int]], List[SupportsRichComparisonT]]"
reveal_type(s)
# Should be Strategy[list[int]], got Strategy[list[SupportsRichComparisonT`-1]]

