from typing import Final

spam: Final = "spam: {eggs}"
spam_eggs = spam.format(eggs="EGGS", foo="bar")
