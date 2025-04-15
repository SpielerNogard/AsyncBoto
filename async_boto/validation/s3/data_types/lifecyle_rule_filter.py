from pydantic import BaseModel

from .lifecycle_rule_and_operator import LifecycleRuleAndOperator
from .tag import Tag


class LifecycleRuleFilter(BaseModel):
    """
    The Filter is used to identify objects that a Lifecycle Rule applies to.
    A Filter can have exactly one of
    Prefix, Tag, ObjectSizeGreaterThan, ObjectSizeLessThan, or And specified. If the
    Filter element is left empty,
    the Lifecycle Rule applies to all objects in the bucket.

    Attributes
    ----------
    And : Optional[LifecycleRuleAndOperator]
        Used to apply a logical AND to two or more predicates.
    ObjectSizeGreaterThan : Optional[int]
        Minimum object size to which the rule applies.
    ObjectSizeLessThan : Optional[int]
        Maximum object size to which the rule applies.
    Prefix : Optional[str]
        Prefix identifying one or more objects to which the rule applies.
    Tag : Optional[Tag]
        This tag must exist in the object's tag set in order for the rule to apply.
    """

    And: LifecycleRuleAndOperator | None = None
    ObjectSizeGreaterThan: int | None = None
    ObjectSizeLessThan: int | None = None
    Prefix: str | None = None
    Tag: Tag | None = None
