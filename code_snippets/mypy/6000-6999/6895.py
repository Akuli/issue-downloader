from typing import Callable, Optional, Tuple, Pattern, Union, TypeVar, Generic, Text

S = TypeVar('S')
T = TypeVar('T')
A = TypeVar('A')
B = TypeVar('B')


class ParserState(Generic[S, T]):
    pass


ParseResult = Optional[Tuple[A, ParserState[S, T]]]
Parser = Callable[[ParserState[S, T]], ParseResult[A, S, T]]


# the idea here is that `re` gives a parser that works with `Text` input and produces a bit of `Text` as output, with a bit of parser state `S` regarding which this parser is agnostic.
def re(pat):
    # type: (Union[Text, Pattern]) -> Parser[S, Text, Text]
    raise NotImplementedError


def then(p1, p2):
    # type: (Parser[S, T, A], Parser[S, T, B]) -> Parser[S, T, B]
    raise NotImplementedError


ws = re(u'\\s*')


# this fails to typecheck
def ws_then1(p):
    # type: (Parser[S, Text, A]) -> Parser[S, Text, A]
    return then(ws, p)


# this typechecks
def ws_then2(p):
    # type: (Parser[S, Text, A]) -> Parser[S, Text, A]
    return then(re(u'\\s*'), p)

