from pydantic import BaseModel
from typing import Optional, Literal

class LocationInfo(BaseModel):
    """
    Specifies the location where the bucket will be created.

    Attributes
    ----------
    Name : Optional[str]
        The name of the location where the bucket will be created. For directory buckets, this is the Zone ID
        of the Availability Zone (AZ) or Local Zone (LZ).
    Type : Optional[Literal["AvailabilityZone", "LocalZone"]]
        The type of location where the bucket will be created.
    """
    Name: Optional[str] = None
    Type: Optional[Literal["AvailabilityZone", "LocalZone"]] = None