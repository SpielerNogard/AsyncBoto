from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Part(BaseModel):
    """
    Container for elements related to a part.

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
        Entity tag returned when the part was uploaded.
    LastModified : Optional[datetime]
        Date and time at which the part was uploaded.
    PartNumber : Optional[int]
        Part number identifying the part (1 to 10,000).
    Size : Optional[int]
        Size in bytes of the uploaded part data.
    """
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumCRC64NVME: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
    ETag: Optional[str] = None
    LastModified: Optional[datetime] = None
    PartNumber: Optional[int] = Field(None, ge=1, le=10000)
    Size: Optional[int] = None