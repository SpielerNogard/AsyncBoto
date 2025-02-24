from pydantic import BaseModel, constr, conint
from typing import Optional, Literal
from .auto_scaling_settings_description import AutoScalingSettingsDescription

class ReplicaGlobalSecondaryIndexSettingsDescription(BaseModel):
    """
    Represents the properties of a global secondary index.

    Attributes
    ----------
    IndexName : str
        The name of the global secondary index. The name must be unique among all other indexes on this table.
    IndexStatus : Optional[str]
        The current status of the global secondary index.
    ProvisionedReadCapacityAutoScalingSettings : Optional[AutoScalingSettingsDescription]
        Auto scaling settings for a global secondary index replica's read capacity units.
    ProvisionedReadCapacityUnits : Optional[int]
        The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException.
    ProvisionedWriteCapacityAutoScalingSettings : Optional[AutoScalingSettingsDescription]
        Auto scaling settings for a global secondary index replica's write capacity units.
    ProvisionedWriteCapacityUnits : Optional[int]
        The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException.
    """
    IndexName: constr(min_length=3, max_length=255, pattern=r'[a-zA-Z0-9_.-]+')
    IndexStatus: Optional[Literal['CREATING', 'UPDATING', 'DELETING', 'ACTIVE']] = None
    ProvisionedReadCapacityAutoScalingSettings: Optional[AutoScalingSettingsDescription] = None
    ProvisionedReadCapacityUnits: Optional[conint(ge=1)] = None
    ProvisionedWriteCapacityAutoScalingSettings: Optional[AutoScalingSettingsDescription] = None
    ProvisionedWriteCapacityUnits: Optional[conint(ge=1)] = None