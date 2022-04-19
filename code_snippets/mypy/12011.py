import typing as t

TCallable = t.TypeVar("TCallable", bound=t.Callable[..., t.Any])
P = t.ParamSpec("P")

class X(t.Generic[TCallable]):
  pass  
  
class Y(t.Generic[P], X[t.Callable[P, t.Any]]): # error: The first argument to Callable must be a list of types or "..."
  pass
