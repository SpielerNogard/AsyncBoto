from pydantic import BaseModel
from typing import Optional, Literal
from .grantee import Grantee

class TargetGrant(BaseModel):
    """
    Container for granting information.

    Attributes
    ----------
    Grantee : Optional[Grantee]
        Container for the person being granted permissions.
    Permission : Optional[Literal["FULL_CONTROL", "READ", "WRITE"]]
        Logging permissions assigned to the grantee for the bucket.
    """
    Grantee: Optional[Grantee]
    Permission: Optional[Literal["FULL_CONTROL", "READ", "WRITE"]]