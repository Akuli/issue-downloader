class Pattern:
    def handleMatch(self, m: Match) -> Optional[Union[str, Element]]: ...

class InlineProcessor(Pattern):
    def handleMatch(self, m: Match, data) -> Union[Tuple[Element, int, int], Tuple[None, None, None]]: ...  # type: ignore
