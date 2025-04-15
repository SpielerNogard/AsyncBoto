from typing import Literal

from pydantic import BaseModel

from .replication_time_value import (
    ReplicationTimeValue,  # Assuming ReplicationTimeValue is defined in a separate file
)


class ReplicationTime(BaseModel):
    """
    A container specifying S3 Replication Time Control (S3 RTC) related information,
    including whether S3 RTC is enabled and the time by which replication
    should be complete.

    Attributes
    ----------
    Status : Literal["Enabled", "Disabled"]
        Specifies whether the replication time is enabled.
    Time : ReplicationTimeValue
        A container specifying the time by which replication should be complete
        for all objects.
    """

    Status: Literal["Enabled", "Disabled"]
    Time: ReplicationTimeValue
