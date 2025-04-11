from pydantic import BaseModel
from typing import Optional

class CompletedPart(BaseModel):
    """
    Details of the parts that were uploaded.

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
    PartNumber : Optional[int]
        Part number that identifies the part. Must be a positive integer between 1 and 10,000.
    """
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumCRC64NVME: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
    ETag: Optional[str] = None
    PartNumber: Optional[int] = None