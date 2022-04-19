# test.py
import foo_mod
import foo_mod.bar_mod as bar_mod

class baz(foo_mod.foo, bar_mod.bar):
    pass
