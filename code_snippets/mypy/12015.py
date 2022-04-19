foo: object
if isinstance(foo, list):
    a = foo[1]
    reveal_type(a) # Any
    a.asdfasdfasdf # no error
