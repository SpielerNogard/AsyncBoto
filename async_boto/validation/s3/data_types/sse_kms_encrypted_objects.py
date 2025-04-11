from pydantic import BaseModel
from typing import Literal

class SseKmsEncryptedObjects(BaseModel):
    """
    A container for filter information for the selection of S3 objects encrypted with AWS KMS.

    Attributes
    ----------
    Status : Literal["Enabled", "Disabled"]
        Specifies whether Amazon S3 replicates objects created with server-side encryption
        using an AWS KMS key stored in AWS Key Management Service.
    """
    Status: Literal["Enabled", "Disabled"]