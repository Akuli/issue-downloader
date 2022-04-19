def foo(value: object | str) -> None:
    if callable(value):
        print(1) # Statement is unreachable  [unreachable]
