from pydantic import BaseModel

from .tag import Tag


class MetricsAndOperator(BaseModel):
    """
    A conjunction (logical AND) of predicates, used in evaluating a metrics filter.

    Attributes
    ----------
    AccessPointArn : Optional[str]
        The access point ARN used when evaluating an AND predicate.
    Prefix : Optional[str]
        The prefix used when evaluating an AND predicate.
    Tags : Optional[List[Tag]]
        The list of tags used when evaluating an AND predicate.
    """

    AccessPointArn: str | None = None
    Prefix: str | None = None
    Tags: list[Tag] | None = None
