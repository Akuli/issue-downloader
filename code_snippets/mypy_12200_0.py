class Permissive(TypedDict, total=False):
  id: str

class Restrictive(TypedDict):
  id: str

def convert(d: Restrictive) -> Permissive:
  return cast(Permissive, d)
