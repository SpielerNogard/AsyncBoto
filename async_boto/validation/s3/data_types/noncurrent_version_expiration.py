from pydantic import BaseModel, Field
from typing import Optional

class NoncurrentVersionExpiration(BaseModel):
    """
    Specifies when noncurrent object versions expire. Upon expiration, Amazon S3 permanently deletes
    the noncurrent object versions.

    Attributes
    ----------
    NewerNoncurrentVersions : Optional[int]
        Specifies how many noncurrent versions Amazon S3 will retain. Maximum value is 100.
    NoncurrentDays : Optional[int]
        Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action.
    """
    NewerNoncurrentVersions: Optional[int] = Field(None, le=100)
    NoncurrentDays: Optional[int] = Field(None, gt=0)