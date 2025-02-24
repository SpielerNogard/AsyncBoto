from pydantic import BaseModel, Field
from typing import Optional
from .auto_scaling_target_tracking_scaling_policy_configuration_description import (
    AutoScalingTargetTrackingScalingPolicyConfigurationDescription,
)


class AutoScalingPolicyDescription(BaseModel):
    PolicyName: Optional[str] = Field(
        None, min_length=1, max_length=256, pattern=r"\p{Print}+"
    )
    TargetTrackingScalingPolicyConfiguration: Optional[
        AutoScalingTargetTrackingScalingPolicyConfigurationDescription
    ] = None
