from pydantic import BaseModel

from .analytics_and_operator import AnalyticsAndOperator
from .tag import Tag


class AnalyticsFilter(BaseModel):
    """
    The filter used to describe a set of objects for analyses.

    Attributes
    ----------
    And : Optional[AnalyticsAndOperator]
        A conjunction (logical AND) of predicates, which is used in evaluating an
        analytics filter.
    Prefix : Optional[str]
        The prefix to use when evaluating an analytics filter.
    Tag : Optional[Tag]
        The tag to use when evaluating an analytics filter.
    """

    And: AnalyticsAndOperator | None = None
    Prefix: str | None = None
    Tag: Tag | None = None
