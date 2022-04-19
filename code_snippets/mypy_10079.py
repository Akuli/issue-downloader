import datetime


class Bar:
    def __init__(self, a: int, b: str, c: datetime.datetime):
        pass


class Baz(Bar):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


Baz(b=3)
