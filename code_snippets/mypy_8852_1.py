from django.db import models

class Baz():
    pass

class Foo(Baz):
    pass

class Bar(Baz):
    pass

def f(param: Foo) -> None:
    pass

f(Foo())
f(Bar())
f(Baz())
