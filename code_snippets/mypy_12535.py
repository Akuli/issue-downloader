x = "a"
reveal_type(x)
assert x in ("a", "b", "c")
reveal_type(x)

y = 20
reveal_type(y)
assert y == 10 or y == 20 or y == 50
reveal_type(y)
