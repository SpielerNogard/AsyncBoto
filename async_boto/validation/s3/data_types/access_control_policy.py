from pydantic import BaseModel

from .grant import Grant
from .owner import Owner


class AccessControlList(BaseModel):
    """
    Contains the elements that set the ACL permissions for an object per grantee.
    """

    Grants: list[Grant] | None
    Owner: Owner | None
