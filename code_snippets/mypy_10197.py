class A:
    def foo(self, s: str) -> str: ...

class B(A):
    def foo(self, n: float) -> float: ... # type: ignore

class C(B):
    def foo(self, n: float) -> float: ...

class Pattern:
    def handleMatch(self, m: Match) -> Optional[Union[str, Element]]: ...

class InlineProcessor(Pattern):
    def handleMatch(self, m: Match, data) -> Union[Tuple[Element, int, int], Tuple[None, None, None]]: ...  # type: ignore

