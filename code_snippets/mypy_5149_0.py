from mypy_extensions import TypedDict

Data = TypedDict("Data", {"i": {"j": int}})

def access(data: Data) -> None:
    data["i"]["j"] += 1

mydata = {"i": {"j": 5}}  # type: Data
access(mydata)
