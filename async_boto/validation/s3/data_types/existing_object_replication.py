from typing import Literal

from pydantic import BaseModel


class ExistingObjectReplication(BaseModel):
    """
    Optional configuration to replicate existing source bucket objects.

    Attributes
    ----------
    Status : Literal["Enabled", "Disabled"]
        Specifies whether Amazon S3 replicates existing source bucket objects.
    """

    Status: Literal["Enabled", "Disabled"]
