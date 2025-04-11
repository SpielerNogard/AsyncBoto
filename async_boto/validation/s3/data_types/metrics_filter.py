from pydantic import BaseModel
from typing import Optional
from .metrics_and_operator import MetricsAndOperator
from .tag import Tag

class MetricsFilter(BaseModel):
    """
    Specifies a metrics configuration filter. The metrics configuration only includes objects that meet
    the filter's criteria. A filter must be a prefix, an object tag, an access point ARN, or a conjunction
    (MetricsAndOperator).

    Attributes
    ----------
    AccessPointArn : Optional[str]
        The access point ARN used when evaluating a metrics filter.
    And : Optional[MetricsAndOperator]
        A conjunction (logical AND) of predicates, which is used in evaluating a metrics filter.
    Prefix : Optional[str]
        The prefix used when evaluating a metrics filter.
    Tag : Optional[Tag]
        The tag used when evaluating a metrics filter.
    """
    AccessPointArn: Optional[str] = None
    And: Optional[MetricsAndOperator] = None
    Prefix: Optional[str] = None
    Tag: Optional[Tag] = None