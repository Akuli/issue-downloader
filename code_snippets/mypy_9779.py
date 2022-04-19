@dataclass
class Passport:
    byr: int

    @property
    def byr(self) -> int:
        return self._byr

    @byr.setter
    def byr(self, value) -> None:
        if int(value) < 1920 or int(value) > 2002:
            raise Exception("Birth year must be between 1920 and 2002")
        self._byr = int(value)
