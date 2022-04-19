from hypothesis import strategies as st

st.lists(st.integers()).map(sorted)
# error: Argument to "map" of "SearchStrategy" has incompatible type overloaded function;
#        expected "Callable[[List[int]], List[SupportsRichComparisonT]]"
