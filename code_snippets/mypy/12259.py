# src/foobar/app.py
from .widgets import BlueWidget, RedWidget, Widget, WidgetSpec


class App:
    def make_widget(self, spec: WidgetSpec) -> Widget:
        if spec.color == "red":
            return RedWidget(app=self, spec=spec)
        elif spec.color == "blue":
            return BlueWidget(app=self, spec=spec)
        else:
            raise ValueError(f"Unsupported widget color: {spec.color!r}")

# src/foobar/widgets/base.py
from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import attr

if TYPE_CHECKING:
    from ..app import App


@attr.define
class WidgetSpec:
    color: str
    flavor: str
    nessness: Optional[int]


@attr.define
class Widget:
    app: App
    spec: WidgetSpec

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

