from typing import Literal

from pydantic import BaseModel


class InventorySchedule(BaseModel):
    """
    Specifies the schedule for generating inventory results.

    Attributes
    ----------
    Frequency : Literal["Daily", "Weekly"]
        Specifies how frequently inventory results are produced.
    """

    Frequency: Literal["Daily", "Weekly"]
