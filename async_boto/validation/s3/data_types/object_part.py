from pydantic import BaseModel, Field


class ObjectPart(BaseModel):
    """
    Represents a container for elements related to an individual part.

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
    PartNumber : Optional[int]
        The part number identifying the part (1-10,000).
    Size : Optional[int]
        The size of the uploaded part in bytes.
    """

    ChecksumCRC32: str | None = None
    ChecksumCRC32C: str | None = None
    ChecksumCRC64NVME: str | None = None
    ChecksumSHA1: str | None = None
    ChecksumSHA256: str | None = None
    PartNumber: int | None = Field(None, ge=1, le=10000)
    Size: int | None = None
