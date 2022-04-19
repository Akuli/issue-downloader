class Base:
    @overload
    def A(self, x: str) -> str:
        ...

    @overload
    def A(self, x: int) -> int:
        ...

    def A(self, x: Any) -> Union[str, int]:
        pass


class Derived(Base):
    def A(self, x: Any) -> Union[str, int]:  # Error here!
        pass
