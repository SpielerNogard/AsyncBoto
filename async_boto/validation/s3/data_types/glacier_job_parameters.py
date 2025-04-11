from pydantic import BaseModel
from typing import Literal

class GlacierJobParameters(BaseModel):
    """
    Container for S3 Glacier job parameters.

    Attributes
    ----------
    Tier : Literal["Standard", "Bulk", "Expedited"]
        Retrieval tier at which the restore will be processed.
    """
    Tier: Literal["Standard", "Bulk", "Expedited"]