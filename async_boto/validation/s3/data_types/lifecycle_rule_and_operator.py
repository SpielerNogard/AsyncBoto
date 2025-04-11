from pydantic import BaseModel, Field
from typing import Optional, List
from .tag import Tag

class LifecycleRuleAndOperator(BaseModel):
    """
    This is used in a Lifecycle Rule Filter to apply a logical AND to two or more predicates.
    The Lifecycle Rule will apply to any object matching all of the predicates configured inside the And operator.

    Attributes
    ----------
    ObjectSizeGreaterThan : Optional[int]
        Minimum object size to which the rule applies.
    ObjectSizeLessThan : Optional[int]
        Maximum object size to which the rule applies.
    Prefix : Optional[str]
        Prefix identifying one or more objects to which the rule applies.
    Tags : Optional[List[Tag]]
        All of these tags must exist in the object's tag set in order for the rule to apply.
    """
    ObjectSizeGreaterThan: Optional[int] = None
    ObjectSizeLessThan: Optional[int] = None
    Prefix: Optional[str] = None
    Tags: Optional[List[Tag]] = None