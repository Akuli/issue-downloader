from typing import Callable, Generic, Optional, TypeVar, Union, overload

F = TypeVar("F")
G = TypeVar("G")


class cache_readonly(Generic[F, G]):
    def __init__(self, func: Callable[[F], G]) -> None:
        self.func = func
        self.name = func.__name__
        self.__doc__ = getattr(func, "__doc__", None)

    @overload
    def __get__(self, obj: F, typ) -> G:
        ...

    @overload
    def __get__(self, obj: None, typ) -> "cache_readonly[F, G]":
        ...

    def __get__(self, obj: Optional[F], typ) -> Union[G, "cache_readonly[F, G]"]:
        if obj is None:
            # accessed on the class, not the instance
            return self

        # Get the cache or set a default one if needed
        cache = getattr(obj, "_cache", None)
        if cache is None:
            cache = obj._cache = {}  # type: ignore

        if self.name in cache:
            val = cache[self.name]
        else:
            val = self.func(obj)
            cache[self.name] = val
        return val

    def __set__(self, obj: F, value: G) -> None:
        raise AttributeError("Can't set attribute")


class TestA:
    @cache_readonly
    def x(self) -> str:
        return "A"


class TestB:
    @cache_readonly
    def x(self) -> str:
        return "B"


def test(obj: Union[TestA, TestB]) -> str:
    return obj.x
