from typing import no_type_check, no_type_check_decorator

@no_type_check_decorator
def test(fn):
    return fn

@test
def blah(x: {'x': 1}):
    pass

@no_type_check
def blah2(x: {'x': 1}):
    pass
