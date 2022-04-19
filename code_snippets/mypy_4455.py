d = {}
e = {}

def f():
    d['x'] = 1

d['y'] = 2
e['y'] = 2

reveal_type(d)  # dict[Any, Any]
reveal_type(e)  # dict[str, int]
