from pydantic import BaseModel
from typing import Optional

class Progress(BaseModel):
    """
    This data type contains information about the progress of an operation.

    Attributes
    ----------
    BytesProcessed : Optional[int]
        The current number of uncompressed object bytes processed.
    BytesReturned : Optional[int]
        The current number of bytes of records payload data returned.
    BytesScanned : Optional[int]
        The current number of object bytes scanned.
    """
    BytesProcessed: Optional[int] = None
    BytesReturned: Optional[int] = None
    BytesScanned: Optional[int] = None