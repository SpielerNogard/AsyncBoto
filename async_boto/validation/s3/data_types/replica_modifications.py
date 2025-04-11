from pydantic import BaseModel
from typing import Literal

class ReplicaModifications(BaseModel):
    """
    A filter for selecting modifications on replicas. Specifies whether Amazon S3
    replicates modifications on replicas.

    Attributes
    ----------
    Status : Literal["Enabled", "Disabled"]
        Specifies whether Amazon S3 replicates modifications on replicas.
    """
    Status: Literal["Enabled", "Disabled"]