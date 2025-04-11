from pydantic import BaseModel
from typing import Literal

class AccessControlTranslation(BaseModel):
    """
    A container for information about access control for replicas.
    """
    Owner: Literal["Destination"]