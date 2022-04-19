x = None

def f():
    global x
    x = 1

reveal_type(x)  # Union[Any, None]
