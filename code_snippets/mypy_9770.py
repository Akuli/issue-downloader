from attr import attrs, attrib


@attrs(frozen=True)
class Name:
    name: str = attrib(converter=str.lower)

    def __str__(self) -> str:
        return self.name

