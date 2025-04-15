from pydantic import BaseModel

from .lifecycle_rule import LifecycleRule


class BucketLifecycleConfiguration(BaseModel):
    """
    Specifies the lifecycle configuration for objects in an Amazon S3 bucket.

    Attributes
    ----------
    Rules : List[LifecycleRule]
        A list of lifecycle rules for individual objects in an Amazon S3 bucket.
    """

    Rules: list[LifecycleRule]
