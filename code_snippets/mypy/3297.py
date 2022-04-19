def is_subtype(left, right):
    if isinstance(left, AnyType) or isinstance(right, AnyType):
        return True
    return is_proper_subtype(left, right)
