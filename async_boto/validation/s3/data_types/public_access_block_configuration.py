from pydantic import BaseModel
from typing import Optional

class PublicAccessBlockConfiguration(BaseModel):
    """
    The PublicAccessBlock configuration for an Amazon S3 bucket.

    Attributes
    ----------
    BlockPublicAcls : Optional[bool]
        Specifies whether Amazon S3 should block public ACLs for this bucket and objects.
    BlockPublicPolicy : Optional[bool]
        Specifies whether Amazon S3 should block public bucket policies for this bucket.
    IgnorePublicAcls : Optional[bool]
        Specifies whether Amazon S3 should ignore public ACLs for this bucket and objects.
    RestrictPublicBuckets : Optional[bool]
        Specifies whether Amazon S3 should restrict public bucket policies for this bucket.
    """
    BlockPublicAcls: Optional[bool] = None
    BlockPublicPolicy: Optional[bool] = None
    IgnorePublicAcls: Optional[bool] = None
    RestrictPublicBuckets: Optional[bool] = None