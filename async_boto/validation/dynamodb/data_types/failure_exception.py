from pydantic import BaseModel
from typing import Optional


class FailureException(BaseModel):
    """
    Represents a failure in a contributor insights operation.

    Attributes
    ----------
    ExceptionDescription : Optional[str]
        Description of the failure.
    ExceptionName : Optional[str]
        Exception name.
    """

    ExceptionDescription: Optional[str] = None
    ExceptionName: Optional[str] = None
