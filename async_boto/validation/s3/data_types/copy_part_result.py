from datetime import datetime

from pydantic import BaseModel


class CopyPartResult(BaseModel):
    """
    Container for all response elements of a CopyPart operation.

    Attributes
    ----------
    ChecksumCRC32 : Optional[str]
        The Base64 encoded, 32-bit CRC32 checksum of the part.
    ChecksumCRC32C : Optional[str]
        The Base64 encoded, 32-bit CRC32C checksum of the part.
    ChecksumCRC64NVME : Optional[str]
        The Base64 encoded, 64-bit CRC64NVME checksum of the part.
    ChecksumSHA1 : Optional[str]
        The Base64 encoded, 160-bit SHA1 checksum of the part.
    ChecksumSHA256 : Optional[str]
        The Base64 encoded, 256-bit SHA256 checksum of the part.
    ETag : Optional[str]
        The entity tag of the object.
    LastModified : Optional[datetime]
        The date and time at which the object was uploaded.
    """

    ChecksumCRC32: str | None = None
    ChecksumCRC32C: str | None = None
    ChecksumCRC64NVME: str | None = None
    ChecksumSHA1: str | None = None
    ChecksumSHA256: str | None = None
    ETag: str | None = None
    LastModified: datetime | None = None
