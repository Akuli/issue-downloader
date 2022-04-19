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
