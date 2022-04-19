from typing import Literal, TypedDict, Union


class TaggedTypeA(TypedDict):
    tag: Literal["A"]
    is_a: bool


class TaggedTypeB(TypedDict):
    tag: Literal["B"]


TaggedUnion = Union[TaggedTypeA, TaggedTypeB]

instance_a: TaggedUnion = {"tag": "A", "is_a": True}

if instance_a["tag"] == "A":
    print(f"Am I type a? {instance_a['is_a']}")

if instance_a.get("tag") == "A":
    print(f"Am I type a this time? {instance_a['is_a']}")

