def func(x: Union[A, B]) -> bool:
    if isinstance(x, A):
        return x.permissions_for(x.me)
    else:
        return x.permissions_for(x.me)
