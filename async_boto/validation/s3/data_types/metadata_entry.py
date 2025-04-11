from pydantic import BaseModel
from typing import Optional

class MetadataEntry(BaseModel):
    """
    A metadata key-value pair to store with an object.

    Attributes
    ----------
    Name : Optional[str]
        Name of the object.
    Value : Optional[str]
        Value of the object.
    """
    Name: Optional[str] = None
    Value: Optional[str] = None