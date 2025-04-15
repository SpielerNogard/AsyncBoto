from pydantic import BaseModel


class PublicAccessBlockConfiguration(BaseModel):
    """
    The PublicAccessBlock configuration for an Amazon S3 bucket.

    Attributes
    ----------
    BlockPublicAcls : Optional[bool]
        Specifies whether Amazon S3 should block public ACLs for this bucket and
        objects.
    BlockPublicPolicy : Optional[bool]
        Specifies whether Amazon S3 should block public bucket policies for this
        bucket.
    IgnorePublicAcls : Optional[bool]
        Specifies whether Amazon S3 should ignore public ACLs for this bucket and
        objects.
    RestrictPublicBuckets : Optional[bool]
        Specifies whether Amazon S3 should restrict public bucket policies for
        this bucket.
    """

    BlockPublicAcls: bool | None = None
    BlockPublicPolicy: bool | None = None
    IgnorePublicAcls: bool | None = None
    RestrictPublicBuckets: bool | None = None
