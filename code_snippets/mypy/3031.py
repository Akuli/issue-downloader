T = TypeVar('T')
def f(*x: T) -> Dict[int, T]: pass
x = None
if bool():
    x = f()
reveal_type(x)  # E: Revealed type is 'builtins.None'
