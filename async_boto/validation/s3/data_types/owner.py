from pydantic import BaseModel
from typing import Optional

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
    DisplayName: Optional[str] = None
    ID: Optional[str] = None