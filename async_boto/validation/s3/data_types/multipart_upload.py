from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime
from .initiator import Initiator
from .owner import Owner

class MultipartUpload(BaseModel):
    """
    Container for the MultipartUpload for the Amazon S3 object.

    Attributes
    ----------
    ChecksumAlgorithm : Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256", "CRC64NVME"]]
        The algorithm that was used to create a checksum of the object.
    ChecksumType : Optional[Literal["COMPOSITE", "FULL_OBJECT"]]
        The checksum type that is used to calculate the object’s checksum value.
    Initiated : Optional[datetime]
        Date and time at which the multipart upload was initiated.
    Initiator : Optional[Initiator]
        Identifies who initiated the multipart upload.
    Key : Optional[str]
        Key of the object for which the multipart upload was initiated.
    Owner : Optional[Owner]
        Specifies the owner of the object that is part of the multipart upload.
    StorageClass : Optional[Literal[
        "STANDARD", "REDUCED_REDUNDANCY", "STANDARD_IA", "ONEZONE_IA",
        "INTELLIGENT_TIERING", "GLACIER", "DEEP_ARCHIVE", "OUTPOSTS",
        "GLACIER_IR", "SNOW", "EXPRESS_ONEZONE"
    ]]
        The class of storage used to store the object.
    UploadId : Optional[str]
        Upload ID that identifies the multipart upload.
    """
    ChecksumAlgorithm: Optional[Literal["CRC32", "CRC32C", "SHA1", "SHA256", "CRC64NVME"]] = None
    ChecksumType: Optional[Literal["COMPOSITE", "FULL_OBJECT"]] = None
    Initiated: Optional[datetime] = None
    Initiator: Optional[Initiator] = None
    Key: Optional[str] = Field(None, min_length=1)
    Owner: Optional[Owner] = None
    StorageClass: Optional[Literal[
        "STANDARD", "REDUCED_REDUNDANCY", "STANDARD_IA", "ONEZONE_IA",
        "INTELLIGENT_TIERING", "GLACIER", "DEEP_ARCHIVE", "OUTPOSTS",
        "GLACIER_IR", "SNOW", "EXPRESS_ONEZONE"
    ]] = None
    UploadId: Optional[str] = None