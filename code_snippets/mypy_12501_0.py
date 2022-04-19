test = (1, 2)
test += (3,)  # error: Incompatible types in assignment (expression has type "Tuple[int, int, int]", variable has type "Tuple[int, int]")
