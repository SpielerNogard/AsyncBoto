from pydantic import BaseModel
from typing import Optional
from .storage_class_analysis_data_export import StorageClassAnalysisDataExport

class StorageClassAnalysis(BaseModel):
    """
    Specifies data related to access patterns to be collected and made available to analyze
    the tradeoffs between different storage classes for an Amazon S3 bucket.

    Attributes
    ----------
    DataExport : Optional[StorageClassAnalysisDataExport]
        Specifies how data related to the storage class analysis for an Amazon S3 bucket
        should be exported.
    """
    DataExport: Optional[StorageClassAnalysisDataExport]