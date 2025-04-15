from pydantic import BaseModel


class CommonPrefix(BaseModel):
    """
    Container for all keys between Prefix and the next occurrence of the string
    specified by a delimiter.

    Attributes
    ----------
    Prefix : Optional[str]
        Container for the specified common prefix.
    """

    Prefix: str | None = None
