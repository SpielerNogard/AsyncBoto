from pydantic import BaseModel
from typing import Optional
from .replica_modifications import ReplicaModifications
from .sse_kms_encrypted_objects import SseKmsEncryptedObjects

class SourceSelectionCriteria(BaseModel):
    """
    A container that describes additional filters for identifying the source objects
    that you want to replicate.

    Attributes
    ----------
    ReplicaModifications : Optional[ReplicaModifications]
        A filter for selections for modifications on replicas.
    SseKmsEncryptedObjects : Optional[SseKmsEncryptedObjects]
        A container for filter information for the selection of Amazon S3 objects
        encrypted with AWS KMS.
    """
    ReplicaModifications: Optional[ReplicaModifications]
    SseKmsEncryptedObjects: Optional[SseKmsEncryptedObjects]