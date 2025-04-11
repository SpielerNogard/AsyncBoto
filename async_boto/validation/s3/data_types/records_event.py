from pydantic import BaseModel
from typing import Optional

class RecordsEvent(BaseModel):
    """
    The container for the records event.

    Attributes
    ----------
    Payload : Optional[bytes]
        The byte array of partial, one or more result records, Base64-encoded.
    """
    Payload: Optional[bytes] = None