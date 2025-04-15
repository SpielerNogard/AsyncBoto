from typing import Literal

from pydantic import BaseModel


class PartitionedPrefix(BaseModel):
    """
    Amazon S3 keys for log objects are partitioned in a specific format.

    Attributes
    ----------
    PartitionDateSource : Optional[Literal["EventTime", "DeliveryTime"]]
        Specifies the partition date source for the partitioned prefix.
    """

    PartitionDateSource: Literal["EventTime", "DeliveryTime"] | None = None
