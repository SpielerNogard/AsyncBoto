from pydantic import BaseModel
from typing import Optional, Literal

class DeleteMarkerReplication(BaseModel):
    """
    Specifies whether Amazon S3 replicates delete markers.

    Attributes
    ----------
    Status : Optional[Literal["Enabled", "Disabled"]]
        Indicates whether to replicate delete markers.
    """
    Status: Optional[Literal["Enabled", "Disabled"]] = None