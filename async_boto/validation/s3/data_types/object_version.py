from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from datetime import datetime
from .owner import Owner
from .restore_status import RestoreStatus

class ObjectVersion(BaseModel):
    """
    Represents the version of an object.

    Attributes
    ----------
    ChecksumAlgorithm : Optional[List[Literal["CRC32", "CRC32C", "SHA1", "SHA256", "CRC64NVME"]]]
        The algorithm used to create a checksum of the object.
    ChecksumType : Optional[Literal["COMPOSITE", "FULL_OBJECT"]]
        The checksum type used to calculate the object’s checksum value.
    ETag : Optional[str]
        The entity tag (MD5 hash) of that version of the object.
    IsLatest : Optional[bool]
        Specifies whether the object is the latest version.
    Key : Optional[str]
        The object key (minimum length of 1).
    LastModified : Optional[datetime]
        The date and time when the object was last modified.
    Owner : Optional[Owner]
        Specifies the owner of the object.
    RestoreStatus : Optional[RestoreStatus]
        Specifies the restoration status of an object.
    Size : Optional[int]
        The size of the object in bytes.
    StorageClass : Optional[Literal["STANDARD"]]
        The class of storage used to store the object.
    VersionId : Optional[str]
        The version ID of the object.
    """
    ChecksumAlgorithm: Optional[List[Literal["CRC32", "CRC32C", "SHA1", "SHA256", "CRC64NVME"]]] = None
    ChecksumType: Optional[Literal["COMPOSITE", "FULL_OBJECT"]] = None
    ETag: Optional[str] = None
    IsLatest: Optional[bool] = None
    Key: Optional[str] = Field(None, min_length=1)
    LastModified: Optional[datetime] = None
    Owner: Optional[Owner] = None
    RestoreStatus: Optional[RestoreStatus] = None
    Size: Optional[int] = None
    StorageClass: Optional[Literal["STANDARD"]] = None
    VersionId: Optional[str] = None