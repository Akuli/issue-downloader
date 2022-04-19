from test import FOO

reveal_type(FOO)  # note: Revealed type is "builtins.bool"
if FOO:
    pass
reveal_type(FOO)  # note: Revealed type is "Literal[True]"
