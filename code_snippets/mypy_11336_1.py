from typing import Final

spam: str = "spam: {eggs}"
spam_eggs = spam.format(eggs="EGGS", foo="bar")
