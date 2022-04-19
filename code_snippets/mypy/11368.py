from enum import Enum
class Letter(Enum):
    A = 'A'
    B = 'B'

    @property
    def shout(self) -> str:
        s = {
            self.A: 'Aaaaah',
            self.B: 'Biiiih',
        }
        return s[self]

print(Letter.A.shout)
print(Letter.B.shout)
