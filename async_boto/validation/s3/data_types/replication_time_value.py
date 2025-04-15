from pydantic import BaseModel, Field


class ReplicationTimeValue(BaseModel):
    """
    A container specifying the time value for S3 Replication Time Control (S3 RTC)
    and replication metrics EventThreshold.

    Attributes
    ----------
    Minutes : Optional[int]
        Contains an integer specifying time in minutes. Valid value: 15.
    """

    Minutes: int | None = Field(None, ge=15, le=15)
