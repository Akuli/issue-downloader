# test.py
import re
import attr

@attr.s
class Test:
    foo = attr.ib(converter=re.compile)

test = Test("foo")
