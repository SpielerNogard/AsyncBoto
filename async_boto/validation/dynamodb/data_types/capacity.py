from pydantic import BaseModel
from typing import Optional


class Capacity(BaseModel):
    """
    Represents the amount of provisioned throughput capacity consumed on a table or an index.

    Attributes
    ----------
    CapacityUnits : Optional[float]
        The total number of capacity units consumed on a table or an index.
    ReadCapacityUnits : Optional[float]
        The total number of read capacity units consumed on a table or an index.
    WriteCapacityUnits : Optional[float]
        The total number of write capacity units consumed on a table or an index.
    """

    CapacityUnits: Optional[float] = None
    ReadCapacityUnits: Optional[float] = None
    WriteCapacityUnits: Optional[float] = None
