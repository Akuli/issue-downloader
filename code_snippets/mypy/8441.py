def foo(x: FixedSequence[int, str]) -> int:
    return x[0]

foo((0, ''))
foo([0, ''])
