from pydantic import BaseModel
from typing import Optional, Literal

class AnalyticsS3BucketDestination(BaseModel):
    """
    Contains information about where to publish the analytics results.

    Attributes
    ----------
    Bucket : str
        The Amazon Resource Name (ARN) of the bucket to which data is exported.
    Format : Literal["CSV"]
        Specifies the file format used when exporting data to Amazon S3.
    BucketAccountId : Optional[str]
        The account ID that owns the destination S3 bucket.
    Prefix : Optional[str]
        The prefix to use when exporting data. The prefix is prepended to all results.
    """
    Bucket: str
    Format: Literal["CSV"]
    BucketAccountId: Optional[str] = None
    Prefix: Optional[str] = None