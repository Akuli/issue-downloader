KT = TypeVar("KT", bound=TestKeys)  # or better Test.KEYS

def __getitem__(self, key: KT) -> Test[KT]:
    ...
