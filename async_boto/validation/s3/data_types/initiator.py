from pydantic import BaseModel


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

    DisplayName: str | None
    ID: str | None
