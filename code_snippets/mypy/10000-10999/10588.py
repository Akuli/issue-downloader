list_of_ints: list[int] = [1,2,3]

reveal_type(["a", "b"] or [1,2,3])  # Produces error. Revealed type is 'builtins.list[builtins.str*]'
reveal_type(["a", "b"] or 123)  # Works. Revealed type is 'Union[builtins.list[builtins.str*], Literal[123]?]'
reveal_type(123 or [1,2,3])  # Works. Revealed type is 'Union[Literal[123]?, builtins.list[builtins.int*]]'
reveal_type(["a", "b"] or list_of_ints)  # Works. Revealed type is 'Union[builtins.list[builtins.str*], builtins.list[builtins.int]]'
