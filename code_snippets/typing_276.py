def f(x) -> None:
    reveal_type(x) # Revealed type is 'Any'
def g(x: int):
    pass
reveal_type(g(1)) # Revealed type is 'Any'

def f(x: ...) -> None:
    ...
def g(x: int) -> ...:
    ...
