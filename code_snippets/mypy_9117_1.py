d = {
    'other': 2,
    **foo,  # Argument 1 to "update" of "dict" has incompatible type "Foo"; expected "Mapping[str, int]"
    **dict(foo),  # Argument 1 to "dict" has incompatible type "Foo"; expected "Mapping[str, int]"
}
d.update(foo)  # Argument 1 to "update" of "dict" has incompatible type "Foo"; expected "Mapping[str, int]"
