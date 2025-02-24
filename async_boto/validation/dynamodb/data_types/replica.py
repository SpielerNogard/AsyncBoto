from pydantic import BaseModel, constr
from typing import Optional


class Replica(BaseModel):
    """
    Represents the properties of a replica.

    Attributes
    ----------
    RegionName : Optional[str]
        The Region where the replica needs to be created.
    """

    RegionName: Optional[constr(min_length=1)] = None
