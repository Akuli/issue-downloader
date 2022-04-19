from functools import reduce

tmp = reduce(lambda x, y: x + y, [[1], [2]])
# this works fine
result = list(tmp) 

# but this one produces an error:
#  Unsupported left operand type for + ("Iterable[int]")
result = list(reduce(lambda x, y: x + y, [[1], [2]]))
