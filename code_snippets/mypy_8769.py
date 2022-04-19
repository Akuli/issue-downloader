from typing import Any


class Hidden:

    def __init__(self, z: float, **kwargs: Any):
        super().__init__(**kwargs)
        self.z = z


class Base:

    def __init__(self, x: int, **kwargs: Any):
        super().__init__(**kwargs)
        self.x = x


class Inherited(Base):

    def __init__(self, y: int, **kwargs: Any):
        super().__init__(**kwargs)
        self.y = y


class Final(Inherited, Hidden):
    pass
