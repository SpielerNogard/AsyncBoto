from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ObjectIdentifier(BaseModel):
    """
    Represents a unique identifier for objects.

    Attributes
    ----------
    Key : str
        Key name of the object.
    ETag : Optional[str]
        An entity tag (ETag) assigned to the object.
    LastModifiedTime : Optional[datetime]
        The modification time of the object.
    Size : Optional[int]
        The size of the object in bytes.
    VersionId : Optional[str]
        The version ID of the object.
    """
    Key: str = Field(..., min_length=1)
    ETag: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    Size: Optional[int] = None
    VersionId: Optional[str] = None