from __future__ import annotations
import numpy as np

class my_float:

    def __radd__(self, other: np.float32) -> my_float:
        return my_float()

a = np.float32()
b = np.float32()
reveal_type(a + b)       # Revealed type is "numpy.floating[numpy.typing._32Bit]"

class _FloatOp(Protocol[_NBit1]):
    @overload
    def __call__(self, __other: bool) -> floating[_NBit1]: ...
    @overload
    def __call__(self, __other: int) -> floating[Union[_NBit1, _NBitInt]]: ...
    @overload
    def __call__(self, __other: float) -> floating[Union[_NBit1, _NBitDouble]]: ...
    @overload
    def __call__(
        self, __other: complex
    ) -> complexfloating[Union[_NBit1, _NBitDouble], Union[_NBit1, _NBitDouble]]: ...
    @overload
    def __call__(
        self, __other: Union[integer[_NBit2], floating[_NBit2]]
    ) -> floating[Union[_NBit1, _NBit2]]: ...

if isinstance(forward_item, Instance):
    if forward_item.has_readable_member('__call__'):
        forward_item = self.expr_checker.analyze_external_member_access('__call__',
                                                                        forward_item,
                                                                        context)
