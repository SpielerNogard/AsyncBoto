from pydantic import BaseModel
from typing import Optional

class Initiator(BaseModel):
    """
    Container element that identifies who initiated the multipart upload.

    Attributes
    ----------
    DisplayName : Optional[str]
        Name of the Principal.
    ID : Optional[str]
        Canonical User ID or user ARN value of the principal.
    """
    DisplayName: Optional[str]
    ID: Optional[str]