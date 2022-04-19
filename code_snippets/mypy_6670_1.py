def i_and(left: Union[bool, Container], right: Union[bool, Container]) -> Union[bool, Container]:
    if isinstance(left, bool) and isinstance(right, bool):
        return left and right

    if isinstance(left, bool):
        if left:
            return right
        return False

    if isinstance(right, bool):
        if right:
            return left
        return False

    return left & right
