from typing import Literal

from pydantic import BaseModel


class BucketInfo(BaseModel):
    """
    Specifies the information about the bucket that will be created.

    Attributes
    ----------
    DataRedundancy : Optional[Literal["SingleAvailabilityZone", "SingleLocalZone"]]
        The number of Zone (Availability Zone or Local Zone) that's used for redundancy
        for the bucket.
    Type : Optional[Literal["Directory"]]
        The type of bucket.
    """

    DataRedundancy: Literal["SingleAvailabilityZone", "SingleLocalZone"] | None = None
    Type: Literal["Directory"] | None = None
