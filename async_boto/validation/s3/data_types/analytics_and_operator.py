from pydantic import BaseModel

from .tag import Tag


class AnalyticsAndOperator(BaseModel):
    """
    A conjunction (logical AND) of predicates, used in evaluating a metrics filter.
    """

    Prefix: str | None
    Tags: list[Tag] | None
