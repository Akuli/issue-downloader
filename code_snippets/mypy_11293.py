# test_case.py
from typing import Callable, Iterable, TypeVar, Union

_T = TypeVar("_T")

def _identity(__: _T) -> _T:
    return __

# decr: Callable[[_T], _T] = _identity  # <-- this approach works
DecoratorT = Callable[[_T], _T]
decr: DecoratorT = _identity  # <-- this causes the false positives below

class Result:
    @decr
    def __init__(self):
        pass

res = Result()  # ; reveal_type(res)  # -> Any (should be test_case.Result)

def some_results(op: Callable[[], Union[Result, Iterable[Result]]]) -> Iterable[Result]:
    result_or_results = op()
    results: Iterable[Result]
    if isinstance(result_or_results, Result):
        results = (result_or_results,)  # ; reveal_type(result_or_results)  # -> (should be test_case.Result)
    else:
        results = result_or_results  # ; reveal_type(result_or_results)  # -> Union[test_case.Result, typing.Iterable[test_case.Result]] (should be typing.Iterable[test_case.Result])
    return results

# …
class DecoratorT(Protocol):
    def __call__(self, __: _T) -> _T:
        ...
decr: DecoratorT = _identity  # <-- all good
# …

# test_case.py
from typing import Callable, Iterable, TypeVar, Union
# from test_case_import import decr  # <-- this works
from .test_case_import import decr  # <-- this causes the false positives below 

class Result:
    @decr
    def __init__(self):
        pass

res = Result()  # ; reveal_type(res)  # -> Any (should be test_case.Result)

def some_results(op: Callable[[], Union[Result, Iterable[Result]]]) -> Iterable[Result]:
    result_or_results = op()
    results: Iterable[Result]
    if isinstance(result_or_results, Result):
        results = (result_or_results,)  # ; reveal_type(result_or_results)  # -> (should be test_case.Result)
    else:
        results = result_or_results  # ; reveal_type(result_or_results)  # -> Union[test_case.Result, typing.Iterable[test_case.Result]] (should be typing.Iterable[test_case.Result])
    return results

# test_case_import.py
from typing import Callable, TypeVar
_T = TypeVar("_T")

def _identity(__: _T) -> _T:
    return __

decr: Callable[[_T], _T] = _identity  # <-- doesn't matter how this is defined
