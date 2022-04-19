class Container:
    value: int = 0

    def __init__(self, value: int = 0):
        self.value = value

    def __and__(self, other: 'Container') -> 'Container':
        return add_gate_to_cnf('and', self.value, other.value)

    def __str__(self) -> str:
        return str(self.value)
