import attr
@attr.s(auto_attribs=True, slots=True)
class UpperString():
    """Uppercase string."""
    value: str = attr.ib(converter=str.upper)
