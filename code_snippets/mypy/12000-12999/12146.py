a: object
if isinstance(a, list):
    reveal_type(a) # list[Any]
    b = a[0] # Any
