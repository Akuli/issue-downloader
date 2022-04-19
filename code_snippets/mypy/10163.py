from typing import Mapping, Optional

FOO: str = "foo"

def func(text: str) -> None:
    _ = text

data: Mapping[str, Optional[str]] = {FOO: "bar"}

if data[FOO] is not None:
    func(data[FOO])  # Line 11

if data["foo"] is not None:
    func(data["foo"])
