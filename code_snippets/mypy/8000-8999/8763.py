from typing import AnyStr, Generic


class A(Generic[AnyStr]):
    def __init__(self, arg: AnyStr):
        # Case A... error: Need type annotation for 'attr'
        self.attr = arg

        reveal_type(arg)
        # note: Revealed type is 'builtins.str*'
        # note: Revealed type is 'builtins.bytes*'

        reveal_type(self.attr)
        # note: Revealed type is 'builtins.str'
        # note: Revealed type is 'Any'
        # Observation: 'builtins.bytes*' doesn't seem to propagate


class B(Generic[AnyStr]):
    def __init__(self, arg: AnyStr):
        # Case B... Success
        self.attr = arg  # type: AnyStr

