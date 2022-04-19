# test.py
from enum import Enum

class Food(Enum):
    SPAM = "spam"
    HAM = "ham"

    def is_spam(self) -> bool:
        return self is self.SPAM

print(Food.SPAM.is_spam())
print(Food.HAM.is_spam())

def is_spam(self) -> bool:
    return self is Food.SPAM
