from pydantic import BaseModel, Field
from typing import Optional
from typing_extensions import Literal
from .abort_incomplete_multipart_upload import AbortIncompleteMultipartUpload
from .lifecycle_expiration import LifecycleExpiration
from .noncurrent_version_expiration import NoncurrentVersionExpiration
from .noncurrent_version_transition import NoncurrentVersionTransition
from .transition import Transition

class Rule(BaseModel):
    """
    Specifies lifecycle rules for an Amazon S3 bucket.

    Attributes
    ----------
    Prefix : str
        Object key prefix that identifies one or more objects to which this rule applies.
    Status : Literal["Enabled", "Disabled"]
        If Enabled, the rule is currently being applied. If Disabled, the rule is not currently being applied.
    AbortIncompleteMultipartUpload : Optional[AbortIncompleteMultipartUpload]
        Specifies the days since the initiation of an incomplete multipart upload before removal.
    Expiration : Optional[LifecycleExpiration]
        Specifies the expiration for the lifecycle of the object.
    ID : Optional[str]
        Unique identifier for the rule. The value can't be longer than 255 characters.
    NoncurrentVersionExpiration : Optional[NoncurrentVersionExpiration]
        Specifies when noncurrent object versions expire.
    NoncurrentVersionTransition : Optional[NoncurrentVersionTransition]
        Specifies when noncurrent objects transition to another storage class.
    Transition : Optional[Transition]
        Specifies when an object transitions to a specified storage class.
    """
    Prefix: str
    Status: Literal["Enabled", "Disabled"]
    AbortIncompleteMultipartUpload: Optional[AbortIncompleteMultipartUpload]
    Expiration: Optional[LifecycleExpiration]
    ID: Optional[str] = Field(None, max_length=255)
    NoncurrentVersionExpiration: Optional[NoncurrentVersionExpiration]
    NoncurrentVersionTransition: Optional[NoncurrentVersionTransition]
    Transition: Optional[Transition]