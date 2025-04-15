from datetime import datetime

from pydantic import BaseModel


class Bucket(BaseModel):
    """
    Represents a bucket resource.

    Attributes
    ----------
    BucketRegion : Optional[str]
        The AWS region where the bucket is located.
    CreationDate : Optional[datetime]
        The date the bucket was created.
    Name : Optional[str]
        The name of the bucket.
    """

    BucketRegion: str | None = None
    CreationDate: datetime | None = None
    Name: str | None = None
