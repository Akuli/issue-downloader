def make_upper(i):
    args = [a.upper() for a in i]
    
    if isinstance(i, set):
        return set(args)
    else:
        return args
