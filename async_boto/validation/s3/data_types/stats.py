from pydantic import BaseModel
from typing import Optional

class Stats(BaseModel):
    """
    Container for the stats details.

    Attributes
    ----------
    BytesProcessed : Optional[int]
        The total number of uncompressed object bytes processed.
    BytesReturned : Optional[int]
        The total number of bytes of records payload data returned.
    BytesScanned : Optional[int]
        The total number of object bytes scanned.
    """
    BytesProcessed: Optional[int]
    BytesReturned: Optional[int]
    BytesScanned: Optional[int]