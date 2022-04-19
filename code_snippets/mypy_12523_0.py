from enum import Enum


class Example(str, Enum):
    ACCOUNT = "account"
    ACCOUNT_2 = "account_2"
    
    def t(self) -> None:
        print(example_map.get(self.value))


example_map = {
    Example.ACCOUNT: 1,
    Example.ACCOUNT_2: 2,
}
