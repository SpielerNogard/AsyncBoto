from typing import Literal

from pydantic import BaseModel


class OwnershipControlsRule(BaseModel):
    """
    The container element for an ownership control rule.

    Attributes
    ----------
    ObjectOwnership : Literal["BucketOwnerPreferred", "ObjectWriter", "BucketOwnerEnforced"]
        The container element for object ownership for a bucket's ownership controls.
    """  # noqa: E501

    ObjectOwnership: Literal[
        "BucketOwnerPreferred", "ObjectWriter", "BucketOwnerEnforced"
    ]
