from pydantic import BaseModel
from typing import List, Optional
from .object_identifier import ObjectIdentifier

class Delete(BaseModel):
    """
    Container for the objects to delete.

    Attributes
    ----------
    Objects : List[ObjectIdentifier]
        The objects to delete.
    Quiet : Optional[bool]
        Element to enable quiet mode for the request. Defaults to None.
    """
    Objects: List[ObjectIdentifier]
    Quiet: Optional[bool] = None