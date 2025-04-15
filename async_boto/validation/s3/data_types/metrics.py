from typing import Literal

from pydantic import BaseModel

from .replication_time_value import ReplicationTimeValue


class Metrics(BaseModel):
    """
    A container specifying replication metrics-related settings enabling replication
    metrics and events.

    Attributes
    ----------
    Status : Literal["Enabled", "Disabled"]
        Specifies whether the replication metrics are enabled.
    EventThreshold : Optional[ReplicationTimeValue]
        A container specifying the time threshold for emitting the
        s3:Replication:OperationMissedThreshold event.
    """

    Status: Literal["Enabled", "Disabled"]
    EventThreshold: ReplicationTimeValue | None = None
