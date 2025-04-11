from pydantic import BaseModel
from typing import Literal
from .analytics_export_destination import AnalyticsExportDestination

class StorageClassAnalysisDataExport(BaseModel):
    """
    Container for data related to the storage class analysis for an Amazon S3 bucket for export.

    Attributes
    ----------
    Destination : AnalyticsExportDestination
        The place to store the data for an analysis.
    OutputSchemaVersion : Literal["V_1"]
        The version of the output schema to use when exporting data. Must be V_1.
    """
    Destination: AnalyticsExportDestination
    OutputSchemaVersion: Literal["V_1"]