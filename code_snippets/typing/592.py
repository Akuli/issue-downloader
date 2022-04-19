def foo(x: Tuple[int, str]) -> None:
    a, b = x

def bar(x: Tuple[int, str]) -> None:
    a = x[0]
    b = x[1]

class Iter:
    def __iter__(self):
        yield 1
        yield ""

foo((1, ""))
foo([1, ""])
foo(Iter())
bar((1, ""))
bar([1, ""])

def foo(x: TupleLike[str, str]): ...
x: List[str] = ...
foo(x)
