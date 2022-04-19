from typing import Any

from xxx.commands import XxxBaseCommand


class Command(XxxBaseCommand):
    def handle(  # type: ignore[override]
        self,
        a: int,
        b: str,
        c: str,
        *args: Any,
        **options: Any,
    ) -> None:
        pass
