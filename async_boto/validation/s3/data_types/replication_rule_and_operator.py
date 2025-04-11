from pydantic import BaseModel
from typing import Optional, List
from .tag import Tag  # Assuming Tag is defined in a separate file

class ReplicationRuleAndOperator(BaseModel):
    """
    A container for specifying rule filters. The filters determine the subset of objects
    to which the rule applies. This element is required only if you specify more than one filter.

    Attributes
    ----------
    Prefix : Optional[str]
        An object key name prefix that identifies the subset of objects to which the rule applies.
    Tags : Optional[List[Tag]]
        An array of tags containing key and value pairs.
    """
    Prefix: Optional[str] = None
    Tags: Optional[List[Tag]] = None