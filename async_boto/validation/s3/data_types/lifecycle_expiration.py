from datetime import datetime

from pydantic import BaseModel, Field


class LifecycleExpiration(BaseModel):
    """
    Container for the expiration for the lifecycle of the object.

    Attributes
    ----------
    Date : Optional[datetime]
        Indicates at what date the object is to be moved or deleted. The date value
        must conform
        to the ISO 8601 format. The time is always midnight UTC.
    Days : Optional[int]
        Indicates the lifetime, in days, of the objects that are subject to the rule.
        The value
        must be a non-zero positive integer.
    ExpiredObjectDeleteMarker : Optional[bool]
        Indicates whether Amazon S3 will remove a delete marker with no noncurrent
        versions.
        This cannot be specified with Days or Date in a Lifecycle Expiration Policy.
    """

    Date: datetime | None = Field(None)
    Days: int | None = Field(None, gt=0)
    ExpiredObjectDeleteMarker: bool | None = Field(None)
