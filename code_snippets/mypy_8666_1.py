import itertools
import typing
itertools.starmap(
    lambda x, y: True, typing.cast(typing.Iterable[typing.Tuple[int, int]],
                                   filter(lambda in_deg: in_deg[1], [(1, 2)])))
