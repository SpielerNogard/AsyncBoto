from datetime import datetime
from typing import Literal

from pydantic import BaseModel


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

    Mode: Literal["GOVERNANCE", "COMPLIANCE"] | None = None
    RetainUntilDate: datetime | None = None
