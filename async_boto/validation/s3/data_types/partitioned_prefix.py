from pydantic import BaseModel
from typing import Optional, Literal

class PartitionedPrefix(BaseModel):
    """
    Amazon S3 keys for log objects are partitioned in a specific format.

    Attributes
    ----------
    PartitionDateSource : Optional[Literal["EventTime", "DeliveryTime"]]
        Specifies the partition date source for the partitioned prefix.
    """
    PartitionDateSource: Optional[Literal["EventTime", "DeliveryTime"]] = None