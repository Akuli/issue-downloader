a: int
b = 1
if isinstance(a, bool):
    reveal_locals()  # "b: int", I would expect "a: bool, b: int"
    reveal_type(a)  # "a: bool" ✔
    
def foo(a: int) -> None:
    b: int
    reveal_locals()  # "a: int, b: int", this is correct, but inconsistent with top level
    reveal_type(a)

a: int = 1
reveal_locals() # nothing 😥

