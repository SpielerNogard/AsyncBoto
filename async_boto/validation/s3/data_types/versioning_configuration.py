from typing import Literal

from pydantic import BaseModel


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

    MFADelete: Literal["Enabled", "Disabled"] | None
    Status: Literal["Enabled", "Suspended"] | None
