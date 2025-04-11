from pydantic import BaseModel
from typing import Optional

class CommonPrefix(BaseModel):
    """
    Container for all keys between Prefix and the next occurrence of the string specified by a delimiter.

    Attributes
    ----------
    Prefix : Optional[str]
        Container for the specified common prefix.
    """
    Prefix: Optional[str] = None