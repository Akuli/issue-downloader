class LinkageCriterion(enum.Enum):
    WARD = "ward"
    COMPLETE = "complete"
    AVERAGE = "average"
    SINGLE = "single"


LinkageCriterionLike = Union[
    LinkageCriterion,
    Literal["ward", "complete", "average", "single"]
]
