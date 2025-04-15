from pydantic import BaseModel


class PolicyStatus(BaseModel):
    """
    The container element for a bucket's policy status.

    Attributes
    ----------
    IsPublic : Optional[bool]
        The policy status for this bucket. TRUE indicates that this bucket is public.
        FALSE indicates that the bucket is not public.
    """

    IsPublic: bool | None = None
