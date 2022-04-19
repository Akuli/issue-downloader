from typing import Final

spam: Final[str] = "spam: {eggs}"
spam_eggs = spam.format(eggs="EGGS", foo="bar")
