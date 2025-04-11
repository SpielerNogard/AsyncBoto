from pydantic import BaseModel
from typing import List
from .tag import Tag

class Tagging(BaseModel):
    """
    Container for TagSet elements.

    Attributes
    ----------
    TagSet : List[Tag]
        A collection for a set of tags.
    """
    TagSet: List[Tag]