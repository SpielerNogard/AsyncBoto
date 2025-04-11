from pydantic import BaseModel, Field

class ErrorDocument(BaseModel):
    """
    The error information.

    Attributes
    ----------
    Key : str
        The object key name to use when a 4XX class error occurs.
    """
    Key: str = Field(..., min_length=1)