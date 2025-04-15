from pydantic import BaseModel

from .ownership_controls_rule import OwnershipControlsRule


class OwnershipControls(BaseModel):
    """
    The container element for a bucket's ownership controls.

    Attributes
    ----------
    Rules : List[OwnershipControlsRule]
        The container element for an ownership control rule.
    """

    Rules: list[OwnershipControlsRule]
