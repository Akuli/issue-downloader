from typing import Callable, Optional, Type

from mypy.plugin import MethodContext, Plugin


class DummyPlugin(Plugin):

    def get_method_hook(
            self, fullname: str) -> Optional[Callable[[MethodContext], Type]]:
        return dummy_callback


def dummy_callback(ctx: MethodContext) -> Type:
    return ctx.default_return_type


plugin = lambda _: DummyPlugin
