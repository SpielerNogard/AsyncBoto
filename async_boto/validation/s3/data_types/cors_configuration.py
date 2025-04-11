from pydantic import BaseModel
from typing import List
from .cors_rule import CORSRule

class CORSConfiguration(BaseModel):
    """
    Describes the cross-origin access configuration for objects in an Amazon S3 bucket.

    Attributes
    ----------
    CORSRules : List[CORSRule]
        A set of origins and methods (cross-origin access) that you want to allow.
        You can add up to 100 rules to the configuration.
    """
    CORSRules: List[CORSRule]