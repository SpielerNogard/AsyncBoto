from pydantic import BaseModel


class Error(BaseModel):
    """
    Container for all error elements.

    Attributes
    ----------
    Code : Optional[str]
        The error code that uniquely identifies an error condition.
    Key : Optional[str]
        The error key.
    Message : Optional[str]
        A generic description of the error condition in English.
    VersionId : Optional[str]
        The version ID of the error.
    """

    Code: str | None = None
    Key: str | None = None
    Message: str | None = None
    VersionId: str | None = None
