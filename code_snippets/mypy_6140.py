@overload
def deco(f: Callable[[], int]) -> Callable[[], str]: ...
@overload
def deco(f: Callable[..., int]) -> Callable[..., str]: ...
def deco(f):
    pass
