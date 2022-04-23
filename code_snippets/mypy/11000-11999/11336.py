from typing import Final

spam: Final[str] = "spam: {eggs}"
spam_eggs = spam.format(eggs="EGGS", foo="bar")

from typing import Final

spam: str = "spam: {eggs}"
spam_eggs = spam.format(eggs="EGGS", foo="bar")

spam = "spam: {eggs}"
spam_eggs = spam.format(eggs="EGGS", foo="bar")

from typing import Final

spam: Final = "spam: {eggs}"
spam_eggs = spam.format(eggs="EGGS", foo="bar")
