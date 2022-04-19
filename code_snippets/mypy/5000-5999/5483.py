import enum

class A(enum.Enum):
    """Docstring"""

reveal_type(A.__doc__)   # <string>:7: error: Revealed type is '__main__.A'
