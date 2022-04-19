import re
import attr

@attr.s(auto_attribs=True)
class GHRepo:
    owner: str
    name: str


def parse_ghrepo(s: str) -> GHRepo:
    if (m := re.fullmatch(r'([^/]+)/([^/]+)', s)) is not None:
        return GHRepo(owner=m[1], name=m[2])
    else:
        raise ValueError(s)


@attr.s
class Foo:
    repo: GHRepo = attr.ib(converter=parse_ghrepo, on_setattr=attr.setters.convert)

f = Foo("owner/name")
f.repo = "python/mypy"  # mypy errors on this line
print(f)
