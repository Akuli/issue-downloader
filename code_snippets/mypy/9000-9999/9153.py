type_hints = typing.get_type_hints(...)  # Dict[str, Any]
if k in type_hints:
    ...

origin = typing.get_origin(...)  # Any
if origin is Literal:
    ...
elif origin is list:
    ...

