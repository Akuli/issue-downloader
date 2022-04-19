import enum
import operator

OperatorEnum = enum.Enum(
    "OperatorEnum",
    {"==": operator.eq, ">=": operator.ge, "<=": operator.le, ">": operator.gt, "<": operator.lt},
)

OperatorEnum["foo"]  # pass, but should throw an error?
OperatorEnum.foo  # Fails
