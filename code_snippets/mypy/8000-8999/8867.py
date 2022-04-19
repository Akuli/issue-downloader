from typing import *

K = TypeVar("K", bound=Hashable)
V = TypeVar("V")


@overload
def dict_get_factory(dictionary: Dict[K, V], 
                     key: K, 
                     factory: Callable[[], V], 
                     takes_key: Literal[False]) -> V: ...

@overload
def dict_get_factory(dictionary: Dict[K, V], 
                     key: K, 
                     factory: Callable[[K], V], 
                     takes_key: Literal[True]) -> V: ...

def dict_get_factory(dictionary: Dict[K, V], 
                     key: K, 
                     factory: Union[Callable[[], V], Callable[[K], V]], 
                     takes_key: bool=False) -> V:
    """Like dict.setdefault(), but uses a factory

    >>> dict_get_factory(d := {}, "foo", int)
    0
    >>> dict_get_factory(d, "bar", lambda key: len(key), takes_key=True)
    3
    >>> d
    {'foo': 0, 'bar': 3}
    """
    try:
        return dictionary[key]
    except KeyError:
        return dictionary.setdefault(key, 
                factory(key) if takes_key else factory())
                
i1: int = dict_get_factory({"foo": 1}, "bar", lambda: 1, False)   # ok
i2: int = dict_get_factory({"foo": 1}, "bar", lambda s: 1, True)  # ok
