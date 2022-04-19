def func(o: object) -> None:
    if o: ...  # error: "o" has type "object" which does not implement __bool__ or __len__ so it could always be true in boolean context  [truthy-bool]
