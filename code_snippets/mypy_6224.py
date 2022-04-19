NT = TypeVar('NT', int, float)
NTU = Union['KspVar[NT]', 'AstBase[NT]', 'ProcessNum[NT]', NT]


class AstOperatorUnary(AstBase[NT], ProcessNum[NT]):
    arg1: NTU[NT]
    string: ClassVar[str]
    priority: ClassVar[int]

    def __init__(self, arg1: NTU[NT]) -> None:
        self.arg1: NTU[NT] = arg1
        self.arg1_pure: NT = get_value(arg1)
        self.arg1_str: str = get_compiled(arg1)


class AstOperatorDouble(AstOperatorUnary[NT]):
    arg2: NTU[NT]

    def __init__(self, arg1: NTU[NT], arg2: NTU[NT]) -> None:
        super().__init__(arg1)
        self.arg2 = arg2
        self.arg2_pure: NT = get_value(arg2)
        self.arg2_str: str = get_compiled(arg2)

__init__
