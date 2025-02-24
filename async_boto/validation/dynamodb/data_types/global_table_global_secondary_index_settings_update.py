from pydantic import BaseModel, constr, conint
from typing import Optional
from .auto_scaling_settings_update import AutoScalingSettingsUpdate


class GlobalTableGlobalSecondaryIndexSettingsUpdate(BaseModel):
    """
    Represents the settings of a global secondary index for a global table that will be modified.

    Attributes
    ----------
    IndexName : constr(min_length=3, max_length=255, regex=r'[a-zA-Z0-9_.-]+')
        The name of the global secondary index. The name must be unique among all other indexes on this table.
    ProvisionedWriteCapacityAutoScalingSettingsUpdate : Optional[AutoScalingSettingsUpdate]
        Auto scaling settings for managing a global secondary index's write capacity units.
    ProvisionedWriteCapacityUnits : Optional[conint(ge=1)]
        The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException.
    """

    IndexName: constr(min_length=3, max_length=255, pattern=r"[a-zA-Z0-9_.-]+")
    ProvisionedWriteCapacityAutoScalingSettingsUpdate: Optional[
        AutoScalingSettingsUpdate
    ] = None
    ProvisionedWriteCapacityUnits: Optional[conint(ge=1)] = None
