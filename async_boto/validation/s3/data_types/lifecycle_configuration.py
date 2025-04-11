from pydantic import BaseModel
from typing import List
from .rule import Rule

class LifecycleConfiguration(BaseModel):
    """
    Container for lifecycle rules. You can add as many as 1000 rules.

    Attributes
    ----------
    Rules : List[Rule]
        Specifies lifecycle configuration rules for an Amazon S3 bucket.
    """
    Rules: List[Rule]