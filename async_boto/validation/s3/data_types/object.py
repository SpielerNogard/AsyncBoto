from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from datetime import datetime
from .owner import Owner
from .restore_status import RestoreStatus

class Object(BaseModel):
    """
    Represents an object consisting of data and its descriptive metadata.

    Attributes
    ----------
    ChecksumAlgorithm : Optional[List[Literal["CRC32", "CRC32C", "SHA1", "SHA256", "CRC64NVME"]]]
        The algorithm that was used to create a checksum of the object.
    ChecksumType : Optional[Literal["COMPOSITE", "FULL_OBJECT"]]
        The checksum type used to calculate the object’s checksum value.
    ETag : Optional[str]
        The entity tag, which is a hash of the object.
    Key : Optional[str]
        The name assigned to the object.
    LastModified : Optional[datetime]
        The creation date of the object.
    Owner : Optional[Owner]
        The owner of the object.
    RestoreStatus : Optional[RestoreStatus]
        The restoration status of the object.
    Size : Optional[int]
        The size of the object in bytes.
    StorageClass : Optional[Literal[
        "STANDARD", "REDUCED_REDUNDANCY", "GLACIER", "STANDARD_IA", "ONEZONE_IA",
        "INTELLIGENT_TIERING", "DEEP_ARCHIVE", "OUTPOSTS", "GLACIER_IR", "SNOW", "EXPRESS_ONEZONE"
    ]]
        The class of storage used to store the object.
    """
    ChecksumAlgorithm: Optional[List[Literal["CRC32", "CRC32C", "SHA1", "SHA256", "CRC64NVME"]]] = None
    ChecksumType: Optional[Literal["COMPOSITE", "FULL_OBJECT"]] = None
    ETag: Optional[str] = None
    Key: Optional[str] = Field(None, min_length=1)
    LastModified: Optional[datetime] = None
    Owner: Optional[Owner] = None
    RestoreStatus: Optional[RestoreStatus] = None
    Size: Optional[int] = None
    StorageClass: Optional[Literal[
        "STANDARD", "REDUCED_REDUNDANCY", "GLACIER", "STANDARD_IA", "ONEZONE_IA",
        "INTELLIGENT_TIERING", "DEEP_ARCHIVE", "OUTPOSTS", "GLACIER_IR", "SNOW", "EXPRESS_ONEZONE"
    ]] = None