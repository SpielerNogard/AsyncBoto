from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from .lifecycle_expiration import LifecycleExpiration
from .lifecycle_rule_filter import LifecycleRuleFilter
from .noncurrent_version_expiration import NoncurrentVersionExpiration
from .noncurrent_version_transition import NoncurrentVersionTransition
from .transition import Transition
from .abort_incomplete_multipart_upload import AbortIncompleteMultipartUpload

class LifecycleRule(BaseModel):
    """
    A lifecycle rule for individual objects in an Amazon S3 bucket.

    Attributes
    ----------
    Status : Literal["Enabled", "Disabled"]
        If 'Enabled', the rule is currently being applied. If 'Disabled', the rule is not currently being applied.
    AbortIncompleteMultipartUpload : Optional[AbortIncompleteMultipartUpload]
        Specifies the days since the initiation of an incomplete multipart upload before removal.
    Expiration : Optional[LifecycleExpiration]
        Specifies the expiration for the lifecycle of the object.
    Filter : Optional[LifecycleRuleFilter]
        Used to identify objects that a Lifecycle Rule applies to.
    ID : Optional[str]
        Unique identifier for the rule, up to 255 characters.
    NoncurrentVersionExpiration : Optional[NoncurrentVersionExpiration]
        Specifies when noncurrent object versions expire.
    NoncurrentVersionTransitions : Optional[List[NoncurrentVersionTransition]]
        Specifies the transition rule for noncurrent objects to a specific storage class.
    Prefix : Optional[str]
        Deprecated. Use Filter instead.
    Transitions : Optional[List[Transition]]
        Specifies when an Amazon S3 object transitions to a specified storage class.
    """
    Status: Literal["Enabled", "Disabled"]
    AbortIncompleteMultipartUpload: Optional[AbortIncompleteMultipartUpload]
    Expiration: Optional[LifecycleExpiration]
    Filter: Optional[LifecycleRuleFilter]
    ID: Optional[str] = Field(None, max_length=255)
    NoncurrentVersionExpiration: Optional[NoncurrentVersionExpiration]
    NoncurrentVersionTransitions: Optional[List[NoncurrentVersionTransition]]
    Prefix: Optional[str]  # Deprecated
    Transitions: Optional[List[Transition]]