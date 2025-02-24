from pydantic import BaseModel, conint
from typing import Literal, Optional


class GlobalSecondaryIndexWarmThroughputDescription(BaseModel):
    """
    The description of the warm throughput value on a global secondary index.

    Attributes
    ----------
    ReadUnitsPerSecond : Optional[conint(ge=1)]
        Represents warm throughput read units per second value for a global secondary index.
    Status : Optional[Literal['CREATING', 'UPDATING', 'DELETING', 'ACTIVE']]
        Represents the warm throughput status being created or updated on a global secondary index.
    WriteUnitsPerSecond : Optional[conint(ge=1)]
        Represents warm throughput write units per second value for a global secondary index.
    """

    ReadUnitsPerSecond: Optional[conint(ge=1)] = None
    Status: Optional[Literal["CREATING", "UPDATING", "DELETING", "ACTIVE"]] = None
    WriteUnitsPerSecond: Optional[conint(ge=1)] = None
