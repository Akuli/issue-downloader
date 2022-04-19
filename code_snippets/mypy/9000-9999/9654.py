import typing as T

V = T.TypeVar("V")
V2 = T.TypeVar("V2")

def apply(val: V, func: T.Callable[[V], V2]) -> V2:
	return func(val)

xs = []
apply(0, lambda a: xs.append(a))
