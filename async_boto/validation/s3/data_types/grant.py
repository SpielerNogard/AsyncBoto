from pydantic import BaseModel
from typing import Optional, Literal
from .grantee import Grantee

class Grant(BaseModel):
    """
    Container for grant information.

    Attributes
    ----------
    Grantee : Optional[Grantee]
        The person being granted permissions.
    Permission : Optional[Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"]]
        Specifies the permission given to the grantee.
    """
    Grantee: Optional[Grantee]
    Permission: Optional[Literal["FULL_CONTROL", "WRITE", "WRITE_ACP", "READ", "READ_ACP"]]