from typing import TypeVar

from hypothesis import strategies as st

_Ex = TypeVar("_Ex", covariant=True)


def everything_except(*types: type) -> st.SearchStrategy[_Ex]:
    strategy = st.from_type(type).flatmap(st.from_type)

    return strategy.filter(lambda x: not isinstance(x, types))  # type: ignore
