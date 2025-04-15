from typing import Literal

from pydantic import BaseModel


class Grantee(BaseModel):
    """
    Container for the person being granted permissions.

    Attributes
    ----------
    Type : Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"]
        Type of grantee.
    DisplayName : Optional[str]
        Screen name of the grantee.
    EmailAddress : Optional[str]
        Email address of the grantee.
    ID : Optional[str]
        The canonical user ID of the grantee.
    URI : Optional[str]
        URI of the grantee group.
    """

    Type: Literal["CanonicalUser", "AmazonCustomerByEmail", "Group"]
    DisplayName: str | None
    EmailAddress: str | None
    ID: str | None
    URI: str | None
