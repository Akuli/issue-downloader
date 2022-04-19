def foo(a: int, b: str = '') -> None: ...

foo(1)  # OK
foo(*[1])  # E: Argument 1 to "foo" has incompatible type *List[int]; expected "str"
