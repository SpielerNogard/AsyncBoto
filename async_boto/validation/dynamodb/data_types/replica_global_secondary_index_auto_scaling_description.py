from pydantic import BaseModel, constr
from typing import Optional, Literal
from .auto_scaling_settings_description import AutoScalingSettingsDescription


class ReplicaGlobalSecondaryIndexAutoScalingDescription(BaseModel):
    """
    Represents the auto scaling configuration for a replica global secondary index.

    Attributes
    ----------
    IndexName : Optional[str]
        The name of the global secondary index.
    IndexStatus : Optional[str]
        The current state of the replica global secondary index.
    ProvisionedReadCapacityAutoScalingSettings : Optional[AutoScalingSettingsDescription]
        Represents the auto scaling settings for a global table or global secondary index.
    ProvisionedWriteCapacityAutoScalingSettings : Optional[AutoScalingSettingsDescription]
        Represents the auto scaling settings for a global table or global secondary index.
    """

    IndexName: Optional[
        constr(min_length=3, max_length=255, regex=r"[a-zA-Z0-9_.-]+")
    ] = None
    IndexStatus: Optional[Literal["CREATING", "UPDATING", "DELETING", "ACTIVE"]] = None
    ProvisionedReadCapacityAutoScalingSettings: Optional[
        AutoScalingSettingsDescription
    ] = None
    ProvisionedWriteCapacityAutoScalingSettings: Optional[
        AutoScalingSettingsDescription
    ] = None
