class AttributeDict(Dict[str, Any]):
    # Mypy is failing to realise that self is dict here.
    __setattr__ = dict.__setitem__  # type: ignore[assignment]
