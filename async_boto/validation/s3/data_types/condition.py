from pydantic import BaseModel
from typing import Optional

class Condition(BaseModel):
    """
    A container for describing a condition that must be met for the specified redirect to apply.

    Attributes
    ----------
    HttpErrorCodeReturnedEquals : Optional[str]
        The HTTP error code when the redirect is applied. Both this and KeyPrefixEquals must be true if both are specified.
    KeyPrefixEquals : Optional[str]
        The object key name prefix when the redirect is applied. Both this and HttpErrorCodeReturnedEquals must be true if both are specified.
    """
    HttpErrorCodeReturnedEquals: Optional[str] = None
    KeyPrefixEquals: Optional[str] = None