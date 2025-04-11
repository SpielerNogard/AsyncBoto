from pydantic import BaseModel
from typing import Literal

class OwnershipControlsRule(BaseModel):
    """
    The container element for an ownership control rule.

    Attributes
    ----------
    ObjectOwnership : Literal["BucketOwnerPreferred", "ObjectWriter", "BucketOwnerEnforced"]
        The container element for object ownership for a bucket's ownership controls.
    """
    ObjectOwnership: Literal["BucketOwnerPreferred", "ObjectWriter", "BucketOwnerEnforced"]