@attr.s(auto_attribs=True)
class Foo:
    bars: List[Bar] = attr.ib(
        default=attr.Factory(list),
        converter=default_if_none(default=attr.Factory(list)),
    )
