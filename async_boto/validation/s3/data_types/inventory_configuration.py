from pydantic import BaseModel
from typing import List, Literal, Optional
from .inventory_destination import InventoryDestination
from .inventory_schedule import InventorySchedule
from .inventory_filter import InventoryFilter

class InventoryConfiguration(BaseModel):
    """
    Specifies the inventory configuration for an Amazon S3 bucket.

    Attributes
    ----------
    Destination : InventoryDestination
        Contains information about where to publish the inventory results.
    Id : str
        The ID used to identify the inventory configuration.
    IncludedObjectVersions : Literal["All", "Current"]
        Object versions to include in the inventory list.
    IsEnabled : bool
        Specifies whether the inventory is enabled or disabled.
    Schedule : InventorySchedule
        Specifies the schedule for generating inventory results.
    Filter : Optional[InventoryFilter]
        Specifies an inventory filter.
    OptionalFields : Optional[List[Literal[
        "Size", "LastModifiedDate", "StorageClass", "ETag", "IsMultipartUploaded",
        "ReplicationStatus", "EncryptionStatus", "ObjectLockRetainUntilDate",
        "ObjectLockMode", "ObjectLockLegalHoldStatus", "IntelligentTieringAccessTier",
        "BucketKeyStatus", "ChecksumAlgorithm", "ObjectAccessControlList", "ObjectOwner"
    ]]]
        Contains the optional fields that are included in the inventory results.
    """
    Destination: InventoryDestination
    Id: str
    IncludedObjectVersions: Literal["All", "Current"]
    IsEnabled: bool
    Schedule: InventorySchedule
    Filter: Optional[InventoryFilter]
    OptionalFields: Optional[List[Literal[
        "Size", "LastModifiedDate", "StorageClass", "ETag", "IsMultipartUploaded",
        "ReplicationStatus", "EncryptionStatus", "ObjectLockRetainUntilDate",
        "ObjectLockMode", "ObjectLockLegalHoldStatus", "IntelligentTieringAccessTier",
        "BucketKeyStatus", "ChecksumAlgorithm", "ObjectAccessControlList", "ObjectOwner"
    ]]]