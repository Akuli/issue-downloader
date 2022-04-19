KeyTy = TypeVar("KeyTy")
ValTy = TypeVar("ValTy")
TempTy = TypeVar("TempTy")

class CIDict(Dict[KeyTy, ValTy]):
    @overload
    def pop(self, key: KeyTy) -> ValTy:
        pass

    @overload
    def pop(self, key: KeyTy, default: Union[ValTy, TempTy]) \
            -> Union[ValTy, TempTy]:
        pass

    def pop(self, key: KeyTy, default: Optional[Union[ValTy, TempTy]] = None) \
            -> Union[ValTy, TempTy]:
        pass
