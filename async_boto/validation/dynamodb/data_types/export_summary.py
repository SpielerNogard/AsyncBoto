from pydantic import BaseModel, constr
from typing import Optional
from typing_extensions import Literal


class ExportSummary(BaseModel):
    """
    Summary information about an export task.

    Attributes
    ----------
    ExportArn : Optional[constr(min_length=37, max_length=1024)]
        The Amazon Resource Name (ARN) of the export.
    ExportStatus : Optional[Literal["IN_PROGRESS", "COMPLETED", "FAILED"]]
        Export can be in one of the following states: IN_PROGRESS, COMPLETED, or FAILED.
    ExportType : Optional[Literal["FULL_EXPORT", "INCREMENTAL_EXPORT"]]
        The type of export that was performed.
    """

    ExportArn: Optional[constr(min_length=37, max_length=1024)] = None
    ExportStatus: Optional[Literal["IN_PROGRESS", "COMPLETED", "FAILED"]] = None
    ExportType: Optional[Literal["FULL_EXPORT", "INCREMENTAL_EXPORT"]] = None
