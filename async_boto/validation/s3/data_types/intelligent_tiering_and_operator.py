from pydantic import BaseModel
from typing import Optional, List
from .tag import Tag

class IntelligentTieringAndOperator(BaseModel):
    """
    A container for specifying S3 Intelligent-Tiering filters.

    Attributes
    ----------
    Prefix : Optional[str]
        An object key name prefix that identifies the subset of objects to which the configuration applies.
    Tags : Optional[List[Tag]]
        All of these tags must exist in the object's tag set in order for the configuration to apply.
    """
    Prefix: Optional[str]
    Tags: Optional[List[Tag]]