class Permissive(TypedDict, total=False):
  id: str

class Restrictive(TypedDict):
  id: str

def convert(d: Restrictive) -> Permissive:
  return cast(Permissive, d)

python_version = "3.9"
namespace_packages = true
explicit_package_bases = true
strict = true
