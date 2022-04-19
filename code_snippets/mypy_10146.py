x = object()
if isinstance(x, (int, str)):
    reveal_type(x)      # Union[int, str]
    if isinstance(x, int):
        pass
    reveal_type(x)      # object
