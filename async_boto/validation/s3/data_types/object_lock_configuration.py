from pydantic import BaseModel
from typing import Optional, Literal
from .object_lock_rule import ObjectLockRule

class ObjectLockConfiguration(BaseModel):
    """
    Represents the Object Lock configuration parameters for a bucket.

    Attributes
    ----------
    ObjectLockEnabled : Optional[Literal["Enabled"]]
        Indicates whether the bucket has Object Lock configuration enabled.
    Rule : Optional[ObjectLockRule]
        Specifies the Object Lock rule for the bucket.
    """
    ObjectLockEnabled: Optional[Literal["Enabled"]] = None
    Rule: Optional[ObjectLockRule] = None