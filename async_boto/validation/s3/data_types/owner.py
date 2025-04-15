from pydantic import BaseModel


class Owner(BaseModel):
    """
    Container for the owner's display name and ID.

    Attributes
    ----------
    DisplayName : Optional[str]
        The display name of the owner. Supported in specific AWS Regions.
    ID : Optional[str]
        The ID of the owner.
    """

    DisplayName: str | None = None
    ID: str | None = None
