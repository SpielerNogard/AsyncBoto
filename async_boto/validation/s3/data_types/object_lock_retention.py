from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime

class ObjectLockRetention(BaseModel):
    """
    Represents a Retention configuration for an object.

    Attributes
    ----------
    Mode : Optional[Literal["GOVERNANCE", "COMPLIANCE"]]
        Indicates the Retention mode for the specified object.
    RetainUntilDate : Optional[datetime]
        The date on which this Object Lock Retention will expire.
    """
    Mode: Optional[Literal["GOVERNANCE", "COMPLIANCE"]] = None
    RetainUntilDate: Optional[datetime] = None