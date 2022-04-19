def foo() -> None:
    iterator = map(list, ['hello', 'world'])  # error: Argument 1 to "map" has incompatible type "Type[List[Any]]"; expected "Callable[[str], List[_T]]"
    reveal_type(iterator)
