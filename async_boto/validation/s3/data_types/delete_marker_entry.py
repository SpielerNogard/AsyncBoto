from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from .owner import Owner

class DeleteMarkerEntry(BaseModel):
    """
    Information about the delete marker.

    Attributes
    ----------
    IsLatest : Optional[bool]
        Specifies whether the object is the latest version of an object.
    Key : Optional[str]
        The object key. Must have a minimum length of 1.
    LastModified : Optional[datetime]
        Date and time when the object was last modified.
    Owner : Optional[Owner]
        The account that created the delete marker.
    VersionId : Optional[str]
        Version ID of an object.
    """
    IsLatest: Optional[bool] = None
    Key: Optional[str] = Field(None, min_length=1)
    LastModified: Optional[datetime] = None
    Owner: Optional[Owner] = None
    VersionId: Optional[str] = None