from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

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
    """  # noqa: E501

    ChecksumAlgorithm: (
        list[Literal["CRC32", "CRC32C", "SHA1", "SHA256", "CRC64NVME"]] | None
    ) = None
    ChecksumType: Literal["COMPOSITE", "FULL_OBJECT"] | None = None
    ETag: str | None = None
    Key: str | None = Field(None, min_length=1)
    LastModified: datetime | None = None
    Owner: Owner | None = None
    RestoreStatus: RestoreStatus | None = None
    Size: int | None = None
    StorageClass: (
        Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "GLACIER",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "DEEP_ARCHIVE",
            "OUTPOSTS",
            "GLACIER_IR",
            "SNOW",
            "EXPRESS_ONEZONE",
        ]
        | None
    ) = None
