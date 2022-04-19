def move(command: Iterable[Literal["f", "b", "l", "r"]]) -> None:
    for c in command:
        print(c)

move("ffbblr")

move(["f", "f", "b", "b", "l", "r"])

[mypy]
python_version = 3.9
warn_no_return = True
disallow_untyped_defs=True

