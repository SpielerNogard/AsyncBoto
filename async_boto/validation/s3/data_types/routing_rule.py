from pydantic import BaseModel
from typing import Optional
from .redirect import Redirect  # Assuming this is defined in a separate file
from .condition import Condition  # Assuming this is defined in a separate file

class RoutingRule(BaseModel):
    """
    Specifies the redirect behavior and when a redirect is applied.

    Attributes
    ----------
    Redirect : Redirect
        Container for redirect information.
    Condition : Optional[Condition]
        A container for describing a condition that must be met for the specified redirect to apply.
    """
    Redirect: Redirect
    Condition: Optional[Condition]