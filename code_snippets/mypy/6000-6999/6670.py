class Container:
    value: int = 0

    def __init__(self, value: int = 0):
        self.value = value

    def __and__(self, other: 'Container') -> 'Container':
        return add_gate_to_cnf('and', self.value, other.value)

    def __str__(self) -> str:
        return str(self.value)

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
