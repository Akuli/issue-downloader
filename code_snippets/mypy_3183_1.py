z = List[Y](b)  # Argument 1 to "list" has incompatible type "B"; expected Iterable[Y]
reveal_type(z)  # 'builtins.list[Y*]'
