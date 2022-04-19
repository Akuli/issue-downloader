f = filter(lambda s: s.strip() == "", y)
it = itertools.chain(x, f)
reveal_type(it)
