from typing_extensions import final


class Base(object):
    """Can be sub-classed."""


@final
class Child(Base):
    """Final instance."""
