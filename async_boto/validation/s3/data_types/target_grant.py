from typing import Literal

from pydantic import BaseModel

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

    Grantee: Grantee | None
    Permission: Literal["FULL_CONTROL", "READ", "WRITE"] | None
