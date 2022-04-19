from django.db import models

class Baz():
    pass

class Foo(models.Model):
    pass

class Bar(models.Model):
    pass

def f(param: Foo) -> None:
    pass

f(Foo())
f(Bar())
f(Baz())

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

