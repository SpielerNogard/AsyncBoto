from pydantic import BaseModel, Field
from typing import Optional

class ScanRange(BaseModel):
    """
    Specifies the byte range of the object to get the records from.

    Attributes
    ----------
    Start : Optional[int]
        Specifies the start of the byte range. Must be a non-negative integer.
    End : Optional[int]
        Specifies the end of the byte range. Must be a non-negative integer.
    """
    Start: Optional[int] = Field(None, ge=0)
    End: Optional[int] = Field(None, ge=0)