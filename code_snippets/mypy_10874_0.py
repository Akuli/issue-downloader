@dataclass
class Range:
    start: object
    end: object
    def difference(self):
        return self.end - self.start

a = Range(1, 2)
