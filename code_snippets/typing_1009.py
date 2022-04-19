P = ParamSpec("P")
R = TypeVar("R")

def foo(f: Callable[P, R]) -> Callable[P, List[R]]:  # Here, the parameters are actually P + optional kw-only int x = 3
    def inner(*args: P.args, x: int = 3, **kwargs: P.kwargs) -> List[R]:
        results = []
        for _ in range(x):
          ret = f(*args, **kwargs)
          results.append(ret)
        return results
    return inner

@foo
def bar(p: int):
    return p + 2

bar(5)  # Acceptable
bar(5, x=8)  # Should also be Acceptable

Concatenate[("x", int), P]
