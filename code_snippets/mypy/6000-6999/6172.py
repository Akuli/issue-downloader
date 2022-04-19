import attr


def foo(value):
    return value.split()


@attr.s
class Bar:
    field = attr.ib(default=None, converter=foo)
