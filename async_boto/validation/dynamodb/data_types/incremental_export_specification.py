from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime


class IncrementalExportSpecification(BaseModel):
    """
    Optional object containing the parameters specific to an incremental export.

    Attributes
    ----------
    ExportFromTime : Optional[datetime]
        Time in the past which provides the inclusive start range for the export table's data.
    ExportToTime : Optional[datetime]
        Time in the past which provides the exclusive end range for the export table's data.
    ExportViewType : Optional[Literal['NEW_IMAGE', 'NEW_AND_OLD_IMAGES']]
        The view type that was chosen for the export.
    """

    ExportFromTime: Optional[datetime] = None
    ExportToTime: Optional[datetime] = None
    ExportViewType: Optional[
        Literal["NEW_IMAGE", "NEW_AND_OLD_IMAGES"]
    ] = "NEW_AND_OLD_IMAGES"
