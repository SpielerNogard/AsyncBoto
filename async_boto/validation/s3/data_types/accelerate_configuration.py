from typing import Literal

from pydantic import BaseModel


class AccelerateConfiguration(BaseModel):
    """
    Configures the transfer acceleration state for an Amazon S3 bucket.
    """

    Status: Literal["Enabled", "Suspended"] = None
