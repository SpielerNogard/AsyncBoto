from pydantic import BaseModel, conint
from typing import Optional


class PointInTimeRecoverySpecification(BaseModel):
    """
    Represents the settings used to enable point in time recovery.

    Attributes
    ----------
    PointInTimeRecoveryEnabled : bool
        Indicates whether point in time recovery is enabled (true) or disabled (false) on the table.
    RecoveryPeriodInDays : Optional[int]
        The number of preceding days for which continuous backups are taken and maintained.
    """

    PointInTimeRecoveryEnabled: bool
    RecoveryPeriodInDays: Optional[conint(ge=1, le=35)] = 35
