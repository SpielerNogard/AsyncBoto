from pydantic import BaseModel
from typing import Literal

class AccelerateConfiguration(BaseModel):
    """
    Configures the transfer acceleration state for an Amazon S3 bucket.
    """
    Status: Literal["Enabled", "Suspended"] = None