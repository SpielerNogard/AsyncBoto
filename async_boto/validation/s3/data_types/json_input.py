from typing import Literal

from pydantic import BaseModel


class JSONInput(BaseModel):
    """
    Specifies JSON as object's input serialization format.

    Attributes
    ----------
    Type : Optional[Literal["DOCUMENT", "LINES"]]
        The type of JSON. Valid values: "DOCUMENT" or "LINES".
    """

    Type: Literal["DOCUMENT", "LINES"] | None
