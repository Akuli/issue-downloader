class A(TypedDict):
    a: str

class BC(TypedDict, total=False):
    other: str
    a: str

Spec = Union[A, BC]

class Config(TypedDict):
    prop: Spec

def main_prop(build: Spec) -> None:
    reveal_type(build)
    print(build)

def main_config(config: Config) -> None:
    reveal_type(config["prop"])
    print(config["prop"])

if __name__ == "__main__":
    custom_config = Config({"prop": {"other": "..."}})

    main_prop(custom_config["prop"])
    main_config(custom_config)
