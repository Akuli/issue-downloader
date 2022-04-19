from pyparsing import Literal, Optional

Literal("(") + Optional(Literal(")"))
