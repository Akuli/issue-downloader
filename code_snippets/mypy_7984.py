# mypy: allow-redefinition

def f() -> None:
    x = 0
    print(x)
    x = 'x'

    def g() -> None:
        reveal_type(x)  # int, but should be str
