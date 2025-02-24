from pydantic import BaseModel, Field
from typing import Optional


class AutoScalingTargetTrackingScalingPolicyConfigurationDescription(BaseModel):
    TargetValue: float = Field(..., ge=8.515920e-109, le=1.174271e108)
    DisableScaleIn: Optional[bool] = False
    ScaleInCooldown: Optional[int] = None
    ScaleOutCooldown: Optional[int] = None
