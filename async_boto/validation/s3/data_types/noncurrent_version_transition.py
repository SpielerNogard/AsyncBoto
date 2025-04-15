from typing import Literal

from pydantic import BaseModel, Field


class NoncurrentVersionTransition(BaseModel):
    """
    Container for the transition rule that describes when noncurrent objects
    transition to a different
    storage class.

    Attributes
    ----------
    NewerNoncurrentVersions : Optional[int]
        Specifies how many noncurrent versions Amazon S3 will retain in the
        same storage class before transitioning objects. Maximum value is 100.
    NoncurrentDays : Optional[int]
        Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action.
    StorageClass : Optional[Literal["GLACIER", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "DEEP_ARCHIVE", "GLACIER_IR"]]
        The class of storage used to store the object.
    """  # noqa: E501

    NewerNoncurrentVersions: int | None = Field(None, le=100)
    NoncurrentDays: int | None = Field(None, gt=0)
    StorageClass: (
        Literal[
            "GLACIER",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "DEEP_ARCHIVE",
            "GLACIER_IR",
        ]
        | None
    ) = None
