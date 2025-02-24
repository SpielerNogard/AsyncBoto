from pydantic import BaseModel, constr
from typing import Optional, Literal


class TimeToLiveDescription(BaseModel):
    """
    The description of the Time to Live (TTL) status on the specified table.

    Attributes
    ----------
    AttributeName : Optional[constr(min_length=1, max_length=255)]
        The name of the TTL attribute for items in the table.
    TimeToLiveStatus : Optional[Literal['ENABLING', 'DISABLING', 'ENABLED', 'DISABLED']]
        The TTL status for the table.
    """

    AttributeName: Optional[constr(min_length=1, max_length=255)] = None
    TimeToLiveStatus: Optional[
        Literal["ENABLING", "DISABLING", "ENABLED", "DISABLED"]
    ] = None
