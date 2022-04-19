from typing import Type, List


class NonLiskovChild(Exception):
    """Does not match Exception.__init__() signature"""
    def __init__(self, _some_other_arg: object) -> None:
        super().__init__()


types1 = [TypeError, ValueError]
reveal_type(types1)
# Revealed type is 'builtins.list[def (*args: builtins.object) -> builtins.Exception]'

types2 = [TypeError, NonLiskovChild]
reveal_type(types2)
# Revealed type is 'builtins.list[builtins.type*]'

# When explicitly setting the type, mypy accepts NonLiskovChild as an Exception subtype:
types3: List[Type[Exception]] = [TypeError, NonLiskovChild]
reveal_type(types3)
# Revealed type is 'builtins.list[Type[builtins.Exception]]'
