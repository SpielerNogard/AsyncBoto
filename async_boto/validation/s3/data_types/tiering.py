from pydantic import BaseModel, Field, root_validator
from typing import Literal

class Tiering(BaseModel):
    """
    The S3 Intelligent-Tiering storage class is designed to optimize storage costs by automatically moving data
    to the most cost-effective storage access tier, without additional operational overhead.

    Attributes
    ----------
    AccessTier : Literal["ARCHIVE_ACCESS", "DEEP_ARCHIVE_ACCESS"]
        S3 Intelligent-Tiering access tier.
    Days : int
        The number of consecutive days of no access after which an object will be eligible to be transitioned
        to the corresponding tier.
    """
    AccessTier: Literal["ARCHIVE_ACCESS", "DEEP_ARCHIVE_ACCESS"]
    Days: int = Field(..., ge=90, le=730)

    @root_validator
    def validate_days(cls, values):
        access_tier = values.get("AccessTier")
        days = values.get("Days")
        if access_tier == "ARCHIVE_ACCESS" and days < 90:
            raise ValueError("Days must be at least 90 for ARCHIVE_ACCESS tier.")
        if access_tier == "DEEP_ARCHIVE_ACCESS" and days < 180:
            raise ValueError("Days must be at least 180 for DEEP_ARCHIVE_ACCESS tier.")
        return values