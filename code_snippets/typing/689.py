class PSS(AsymmetricPadding):
    MAX_LENGTH: ClassVar[object]
    def __init__(self, mgf: MGF1, salt_length: Union[int, Literal[MAX_LENGTH]]) -> None: ...

class PSS(AsymmetricPadding):
    MAX_LENGTH: Singleton
    def __init__(self, mgf: MGF1, salt_length: Union[int, MAX_LENGTH]) -> None: ...
