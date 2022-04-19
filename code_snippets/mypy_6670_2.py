def v_and(left: Union[bool, Container], right: Union[bool, Container]) -> Union[bool, Container]:
    lbool = isinstance(left, bool)
    rbool = isinstance(right, bool)

    if lbool and rbool:
        return left and right

    if lbool:
        if left:
            return right
        return False

    if rbool:
        if right:
            return left
        return False

    return left & right
