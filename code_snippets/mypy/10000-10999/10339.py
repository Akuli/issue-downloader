def move(command: Iterable[Literal["f", "b", "l", "r"]]) -> None:
    for c in command:
        print(c)

move("ffbblr")

move(["f", "f", "b", "b", "l", "r"])
