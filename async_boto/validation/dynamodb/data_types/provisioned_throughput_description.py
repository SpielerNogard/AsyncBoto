from pydantic import BaseModel, conint
from typing import Optional
from datetime import datetime


class ProvisionedThroughputDescription(BaseModel):
    """
    Represents the provisioned throughput settings for the table, consisting of read and write capacity units, along with data about increases and decreases.

    Attributes
    ----------
    LastDecreaseDateTime : Optional[datetime]
        The date and time of the last provisioned throughput decrease for this table.
    LastIncreaseDateTime : Optional[datetime]
        The date and time of the last provisioned throughput increase for this table.
    NumberOfDecreasesToday : Optional[int]
        The number of provisioned throughput decreases for this table during this UTC calendar day.
    ReadCapacityUnits : Optional[int]
        The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException.
    WriteCapacityUnits : Optional[int]
        The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException.
    """

    LastDecreaseDateTime: Optional[datetime] = None
    LastIncreaseDateTime: Optional[datetime] = None
    NumberOfDecreasesToday: Optional[int] = None
    ReadCapacityUnits: Optional[conint(ge=0)] = None
    WriteCapacityUnits: Optional[conint(ge=0)] = None
