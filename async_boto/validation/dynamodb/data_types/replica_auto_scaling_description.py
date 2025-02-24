from pydantic import BaseModel, constr
from typing import List, Optional, Literal
from .replica_global_secondary_index_auto_scaling_description import (
    ReplicaGlobalSecondaryIndexAutoScalingDescription,
)
from .auto_scaling_settings_description import AutoScalingSettingsDescription


class ReplicaAutoScalingDescription(BaseModel):
    """
    Represents the auto scaling settings of the replica.

    Attributes
    ----------
    GlobalSecondaryIndexes : Optional[List[ReplicaGlobalSecondaryIndexAutoScalingDescription]]
        Replica-specific global secondary index auto scaling settings.
    RegionName : Optional[str]
        The Region where the replica exists.
    ReplicaProvisionedReadCapacityAutoScalingSettings : Optional[AutoScalingSettingsDescription]
        Represents the auto scaling settings for a global table or global secondary index.
    ReplicaProvisionedWriteCapacityAutoScalingSettings : Optional[AutoScalingSettingsDescription]
        Represents the auto scaling settings for a global table or global secondary index.
    ReplicaStatus : Optional[str]
        The current state of the replica.
    """

    GlobalSecondaryIndexes: Optional[
        List[ReplicaGlobalSecondaryIndexAutoScalingDescription]
    ] = None
    RegionName: Optional[constr(min_length=1)] = None
    ReplicaProvisionedReadCapacityAutoScalingSettings: Optional[
        AutoScalingSettingsDescription
    ] = None
    ReplicaProvisionedWriteCapacityAutoScalingSettings: Optional[
        AutoScalingSettingsDescription
    ] = None
    ReplicaStatus: Optional[
        Literal[
            "CREATING",
            "CREATION_FAILED",
            "UPDATING",
            "DELETING",
            "ACTIVE",
            "REGION_DISABLED",
            "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
        ]
    ] = None
