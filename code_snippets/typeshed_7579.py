foo = sum([True, False])
foo += 1

@overload
def sum(__iterable: Iterable[_SumT]) -> _SumT | Literal[0]: ...
