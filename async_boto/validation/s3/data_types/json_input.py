from pydantic import BaseModel
from typing import Optional, Literal

class JSONInput(BaseModel):
    """
    Specifies JSON as object's input serialization format.

    Attributes
    ----------
    Type : Optional[Literal["DOCUMENT", "LINES"]]
        The type of JSON. Valid values: "DOCUMENT" or "LINES".
    """
    Type: Optional[Literal["DOCUMENT", "LINES"]]