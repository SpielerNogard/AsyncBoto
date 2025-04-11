from pydantic import BaseModel
from typing import Optional, Literal

class VersioningConfiguration(BaseModel):
    """
    Describes the versioning state of an Amazon S3 bucket.

    Attributes
    ----------
    MFADelete : Optional[Literal["Enabled", "Disabled"]]
        Specifies whether MFA delete is enabled in the bucket versioning configuration.
    Status : Optional[Literal["Enabled", "Suspended"]]
        The versioning state of the bucket.
    """
    MFADelete: Optional[Literal["Enabled", "Disabled"]]
    Status: Optional[Literal["Enabled", "Suspended"]]