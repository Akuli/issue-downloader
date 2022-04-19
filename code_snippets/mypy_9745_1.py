from typing import List, NonEmpty


def average(numbers: NonEmpty[List[float]]) -> float:
    """Return the average of a non-empty list of numbers."""
    return sum(numbers) / len(numbers)
