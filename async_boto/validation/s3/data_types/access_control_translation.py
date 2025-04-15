from typing import Literal

from pydantic import BaseModel


class AccessControlTranslation(BaseModel):
    """
    A container for information about access control for replicas.
    """

    Owner: Literal["Destination"]
