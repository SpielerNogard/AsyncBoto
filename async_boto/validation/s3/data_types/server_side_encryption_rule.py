from pydantic import BaseModel
from typing import Optional
from .server_side_encryption_by_default import ServerSideEncryptionByDefault

class ServerSideEncryptionRule(BaseModel):
    """
    Specifies the default server-side encryption configuration.

    Attributes
    ----------
    ApplyServerSideEncryptionByDefault : Optional[ServerSideEncryptionByDefault]
        Specifies the default server-side encryption to apply to new objects in the bucket.
    BucketKeyEnabled : Optional[bool]
        Specifies whether Amazon S3 should use an S3 Bucket Key with server-side encryption using KMS (SSE-KMS) for new objects in the bucket.
    """
    ApplyServerSideEncryptionByDefault: Optional[ServerSideEncryptionByDefault]
    BucketKeyEnabled: Optional[bool]