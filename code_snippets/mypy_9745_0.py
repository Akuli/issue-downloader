from typing import List


def average(numbers: List[float]) -> float:
    """Return the average of a non-empty list of numbers."""
    return sum(numbers) / len(numbers)
