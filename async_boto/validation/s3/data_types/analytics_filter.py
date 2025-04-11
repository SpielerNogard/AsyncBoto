from pydantic import BaseModel
from typing import Optional
from .analytics_and_operator import AnalyticsAndOperator
from .tag import Tag

class AnalyticsFilter(BaseModel):
    """
    The filter used to describe a set of objects for analyses.

    Attributes
    ----------
    And : Optional[AnalyticsAndOperator]
        A conjunction (logical AND) of predicates, which is used in evaluating an analytics filter.
    Prefix : Optional[str]
        The prefix to use when evaluating an analytics filter.
    Tag : Optional[Tag]
        The tag to use when evaluating an analytics filter.
    """
    And: Optional[AnalyticsAndOperator] = None
    Prefix: Optional[str] = None
    Tag: Optional[Tag] = None