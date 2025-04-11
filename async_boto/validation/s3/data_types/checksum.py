from pydantic import BaseModel
from typing import Optional, Literal

class Checksum(BaseModel):
    """
    Contains all the possible checksum or digest values for an object.

    Attributes
    ----------
    ChecksumCRC32 : Optional[str]
        The Base64 encoded, 32-bit CRC32 checksum of the object.
    ChecksumCRC32C : Optional[str]
        The Base64 encoded, 32-bit CRC32C checksum of the object.
    ChecksumCRC64NVME : Optional[str]
        The Base64 encoded, 64-bit CRC64NVME checksum of the object.
    ChecksumSHA1 : Optional[str]
        The Base64 encoded, 160-bit SHA1 digest of the object.
    ChecksumSHA256 : Optional[str]
        The Base64 encoded, 256-bit SHA256 digest of the object.
    ChecksumType : Optional[Literal["COMPOSITE", "FULL_OBJECT"]]
        The checksum type used to calculate the object's checksum value.
    """
    ChecksumCRC32: Optional[str] = None
    ChecksumCRC32C: Optional[str] = None
    ChecksumCRC64NVME: Optional[str] = None
    ChecksumSHA1: Optional[str] = None
    ChecksumSHA256: Optional[str] = None
    ChecksumType: Optional[Literal["COMPOSITE", "FULL_OBJECT"]] = None