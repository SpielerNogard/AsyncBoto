from pydantic import BaseModel, Field
from typing import Optional
from .auto_scaling_target_tracking_scaling_policy_configuration_update import AutoScalingTargetTrackingScalingPolicyConfigurationUpdate

class AutoScalingPolicyUpdate(BaseModel):
    """
    Represents the auto scaling policy to be modified.

    Attributes
    ----------
    TargetTrackingScalingPolicyConfiguration : AutoScalingTargetTrackingScalingPolicyConfigurationUpdate
        Represents a target tracking scaling policy configuration.
    PolicyName : Optional[str]
        The name of the scaling policy. Minimum length of 1. Maximum length of 256.
        Pattern: \p{Print}+
    """
    TargetTrackingScalingPolicyConfiguration: AutoScalingTargetTrackingScalingPolicyConfigurationUpdate
    PolicyName: Optional[str] = Field(None, min_length=1, max_length=256, pattern=r"\p{Print}+")