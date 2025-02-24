from pydantic import BaseModel, Field
from typing import Optional
from .auto_scaling_policy_update import AutoScalingPolicyUpdate


class AutoScalingSettingsUpdate(BaseModel):
    """
    Represents the auto scaling settings to be modified for a global table or global secondary index.

    Attributes
    ----------
    AutoScalingDisabled : Optional[bool]
        Disabled auto scaling for this global table or global secondary index.
    AutoScalingRoleArn : Optional[str]
        Role ARN used for configuring auto scaling policy. Minimum length of 1. Maximum length of 1600.
        Pattern: [\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*
    MaximumUnits : Optional[int]
        The maximum capacity units that a global table or global secondary index should be scaled up to.
        Valid Range: Minimum value of 1.
    MinimumUnits : Optional[int]
        The minimum capacity units that a global table or global secondary index should be scaled down to.
        Valid Range: Minimum value of 1.
    ScalingPolicyUpdate : Optional[AutoScalingPolicyUpdate]
        The scaling policy to apply for scaling target global table or global secondary index capacity units.
    """

    AutoScalingDisabled: Optional[bool] = None
    AutoScalingRoleArn: Optional[str] = Field(
        None,
        min_length=1,
        max_length=1600,
        pattern=r"[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*",
    )
    MaximumUnits: Optional[int] = Field(None, ge=1)
    MinimumUnits: Optional[int] = Field(None, ge=1)
    ScalingPolicyUpdate: Optional[AutoScalingPolicyUpdate] = None
