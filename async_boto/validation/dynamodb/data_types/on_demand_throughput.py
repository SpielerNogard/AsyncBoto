from pydantic import BaseModel, conint
from typing import Optional

class OnDemandThroughput(BaseModel):
    """
    Sets the maximum number of read and write units for the specified on-demand table.

    Attributes
    ----------
    MaxReadRequestUnits : Optional[int]
        Maximum number of read request units for the specified table.
    MaxWriteRequestUnits : Optional[int]
        Maximum number of write request units for the specified table.
    """
    MaxReadRequestUnits: Optional[conint(ge=-1)] = None
    MaxWriteRequestUnits: Optional[conint(ge=-1)] = None