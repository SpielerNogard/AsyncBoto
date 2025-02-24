from pydantic import BaseModel, conint
from typing import Optional


class ProvisionedThroughputOverride(BaseModel):
    """
    Replica-specific provisioned throughput settings. If not specified, uses the source table's provisioned throughput settings.

    Attributes
    ----------
    ReadCapacityUnits : Optional[int]
        Replica-specific read capacity units. If not specified, uses the source table's read capacity settings.
    """

    ReadCapacityUnits: Optional[conint(ge=1)] = None
