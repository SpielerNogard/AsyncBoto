from pydantic import BaseModel, Field
from typing import Literal

class ExistingObjectReplication(BaseModel):
    """
    Optional configuration to replicate existing source bucket objects.

    Attributes
    ----------
    Status : Literal["Enabled", "Disabled"]
        Specifies whether Amazon S3 replicates existing source bucket objects.
    """
    Status: Literal["Enabled", "Disabled"]