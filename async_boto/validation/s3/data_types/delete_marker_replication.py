from typing import Literal

from pydantic import BaseModel


class DeleteMarkerReplication(BaseModel):
    """
    Specifies whether Amazon S3 replicates delete markers.

    Attributes
    ----------
    Status : Optional[Literal["Enabled", "Disabled"]]
        Indicates whether to replicate delete markers.
    """

    Status: Literal["Enabled", "Disabled"] | None = None
