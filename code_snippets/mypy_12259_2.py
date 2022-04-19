# src/foobar/widgets/blue.py
import attr
from .base import Widget


@attr.define
class BlueWidget(Widget):
    nessness: int = attr.field(init=False)

    def __attrs_post_init__(self) -> None:
        if self.spec.nessness is None:
            raise ValueError("Blue widgets must be nessy")
        self.nessness = self.spec.nessness
