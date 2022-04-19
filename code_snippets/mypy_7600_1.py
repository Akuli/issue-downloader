T = TypeVar("T", List[str], Set[str])

def make_upper(i: T) -> T:
    args = [a.upper() for a in i]
    
    if isinstance(i, set):
        return set(args)
    else:
        return args
