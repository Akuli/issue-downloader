from typing import Optional


class Base:
    description: Optional[str]


class MixinWDesc:
    description: str


class SubClass(MixinWDesc, Base):
    description: str


class SomeOtherMixin:
    pass

# succeeds
class ImplementsWOMixin(SubClass):
    pass


# fails
class ImplementsWMixin(SomeOtherMixin, SubClass):
    pass
