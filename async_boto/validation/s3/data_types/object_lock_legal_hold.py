from pydantic import BaseModel
from typing import Optional, Literal

class ObjectLockLegalHold(BaseModel):
    """
    Represents a legal hold configuration for an object.

    Attributes
    ----------
    Status : Optional[Literal["ON", "OFF"]]
        Indicates whether the specified object has a legal hold in place.
    """
    Status: Optional[Literal["ON", "OFF"]] = None