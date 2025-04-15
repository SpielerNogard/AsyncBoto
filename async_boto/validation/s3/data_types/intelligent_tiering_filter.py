from pydantic import BaseModel

from .intelligent_tiering_and_operator import IntelligentTieringAndOperator
from .tag import Tag


class IntelligentTieringFilter(BaseModel):
    """
    The Filter is used to identify objects that the S3 Intelligent-Tiering
    configuration applies to.

    Attributes
    ----------
    And : Optional[IntelligentTieringAndOperator]
        A conjunction (logical AND) of predicates, which is used in evaluating a
        metrics filter.
    Prefix : Optional[str]
        An object key name prefix that identifies the subset of objects to which the
        rule applies.
    Tag : Optional[Tag]
        A container of a key-value name pair.
    """

    And: IntelligentTieringAndOperator | None
    Prefix: str | None
    Tag: Tag | None
