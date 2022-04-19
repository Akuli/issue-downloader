from typing import Callable, Iterable, Optional, Tuple, TypeVar

SourceType = TypeVar("SourceType")
TransformedType = TypeVar("TransformedType")
ProcessedType = TypeVar("ProcessedType")


def simple_transform_process(
    source: Iterable[SourceType],
    transform_callback: Callable[[SourceType], Optional[TransformedType]],
    process_callback: Callable[[TransformedType], ProcessedType],
) -> Iterable[Optional[ProcessedType]]:
    for item in source:
        transformed = transform_callback(item)
        if transformed is None:
            yield None
        else:
            yield process_callback(transformed)


def transform_process(
    source: Iterable[SourceType],
    transform_callback: Callable[[SourceType], Optional[TransformedType]],
    process_callback: Callable[[TransformedType], ProcessedType],
) -> Iterable[Tuple[Optional[TransformedType], Optional[ProcessedType]]]:
    for item in source:
        transformed = transform_callback(item)
        if transformed is None:
            yield None, None
        else:
            yield transformed, process_callback(transformed)


def transform(x: str) -> Optional[int]:
    if x:
        return int(x)
    else:
        return None


def process(x: int) -> float:
    return x / 2


def test_simple_transform_process() -> None:
    assert list(simple_transform_process(["", "2", "3"], transform, process)) == [
        None,
        1,
        1.5,
    ]


def test_transform_process() -> None:
    assert list(transform_process(["", "2", "3"], transform, process)) == [
        (None, None),
        (2, 1),
        (3, 1.5),
    ]
