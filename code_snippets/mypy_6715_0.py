import attr

@attr.s
class MyData:
    is_foo: bool = attr.ib()

    @staticmethod
    def is_foo(string: str) -> bool:
        return False
