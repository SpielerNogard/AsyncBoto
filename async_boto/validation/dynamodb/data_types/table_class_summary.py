from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime


class TableClassSummary(BaseModel):
    """
    Contains details of the table class.

    Attributes
    ----------
    LastUpdateDateTime : Optional[datetime]
        The date and time at which the table class was last updated.
    TableClass : Optional[Literal['STANDARD', 'STANDARD_INFREQUENT_ACCESS']]
        The table class of the specified table.
    """

    LastUpdateDateTime: Optional[datetime] = None
    TableClass: Optional[Literal["STANDARD", "STANDARD_INFREQUENT_ACCESS"]] = None
