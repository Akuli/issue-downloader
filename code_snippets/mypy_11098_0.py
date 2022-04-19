a: type = tuple[int] # no error
b = tuple[int] # no error
c = tuple[int, int] # no error
error: type = tuple[int, int] # error: Type application has too many types (1 expected)
