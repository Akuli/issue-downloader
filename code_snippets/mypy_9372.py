from functools import cmp_to_key

x = [(1, '')]

def f(): pass

reveal_type(cmp_to_key)

x.sort(key=cmp_to_key(lambda x, y: f()))  # Cannot infer type argument 1 of "cmp_to_key"
