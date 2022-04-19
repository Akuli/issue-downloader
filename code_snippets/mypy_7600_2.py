T = TypeVar("T", List[str], Set[str])

def make_upper(i: T) -> T:
    args = [a.upper() for a in i]
    
    if isinstance(i, list):
        return args
    else:
        return set(args)
