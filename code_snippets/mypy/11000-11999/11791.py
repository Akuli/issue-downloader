import typing as tp
import enum

@enum.unique
class ColorIndex(enum.IntEnum):
    BLACK = 0
    GREY = 1
    WHITE = 2

    def _missing_(cls, value: object) -> tp.Any:
        return ColorIndex.BLACK
