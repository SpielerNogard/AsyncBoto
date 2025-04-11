from pydantic import BaseModel
from typing import Literal

class InventorySchedule(BaseModel):
    """
    Specifies the schedule for generating inventory results.

    Attributes
    ----------
    Frequency : Literal["Daily", "Weekly"]
        Specifies how frequently inventory results are produced.
    """
    Frequency: Literal["Daily", "Weekly"]