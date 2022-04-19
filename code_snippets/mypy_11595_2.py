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
