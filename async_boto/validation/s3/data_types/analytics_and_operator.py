from pydantic import BaseModel
from typing import Optional, List
from .tag import Tag

class AnalyticsAndOperator(BaseModel):
    """
    A conjunction (logical AND) of predicates, used in evaluating a metrics filter.
    """
    Prefix: Optional[str]
    Tags: Optional[List[Tag]]