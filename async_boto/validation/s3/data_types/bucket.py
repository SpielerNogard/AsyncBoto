from pydantic import BaseModel
from typing import Optional
from datetime import datetime

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
    BucketRegion: Optional[str] = None
    CreationDate: Optional[datetime] = None
    Name: Optional[str] = None