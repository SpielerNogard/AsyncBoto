from typing import Literal

from pydantic import BaseModel


class ObjectLockLegalHold(BaseModel):
    """
    Represents a legal hold configuration for an object.

    Attributes
    ----------
    Status : Optional[Literal["ON", "OFF"]]
        Indicates whether the specified object has a legal hold in place.
    """

    Status: Literal["ON", "OFF"] | None = None
