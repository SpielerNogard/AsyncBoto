from pydantic import BaseModel
from typing import Optional, List
from .target_grant import TargetGrant
from .target_object_key_format import TargetObjectKeyFormat

class LoggingEnabled(BaseModel):
    """
    Describes where logs are stored and the prefix that Amazon S3 assigns to all log object keys for a bucket.

    Attributes
    ----------
    TargetBucket : str
        Specifies the bucket where you want Amazon S3 to store server access logs.
    TargetPrefix : str
        A prefix for all log object keys.
    TargetGrants : Optional[List[TargetGrant]]
        Container for granting information.
    TargetObjectKeyFormat : Optional[TargetObjectKeyFormat]
        Amazon S3 key format for log objects.
    """
    TargetBucket: str
    TargetPrefix: str
    TargetGrants: Optional[List[TargetGrant]] = None
    TargetObjectKeyFormat: Optional[TargetObjectKeyFormat] = None