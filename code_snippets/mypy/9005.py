import enum


@enum.unique
class MyEnum(enum.Enum):
    FOO = enum.auto()
    BAR = enum.auto()


class MyClass:
    __slots__ = (
        "_my_value",
    )

    _my_value: MyEnum

    def __init__(self) -> None:
        super().__init__()
        self._my_value = MyEnum.FOO

    def do_thing(self) -> None:
        if self._my_value is MyEnum.FOO:
            self._set_my_value_to_bar()
            # self._my_value = MyEnum.BAR
            if self._my_value is MyEnum.BAR:
                print("And yet, the value was BAR!")

    def _set_my_value_to_bar(self) -> None:
        self._my_value = MyEnum.BAR


if __name__ == "__main__":
    x = MyClass()
    x.do_thing()
