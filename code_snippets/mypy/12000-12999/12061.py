from typing import Annotated, ClassVar, Final

class C:
    classvar: Annotated[ClassVar[int], (2, 5)] = 4
    const: Annotated[Final[int], "metadata"] = 4
