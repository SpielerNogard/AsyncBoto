from pydantic import BaseModel
from typing import Optional
from .analytics_and_operator import AnalyticsAndOperator
from .tag import Tag
from .storage_class_analysis import StorageClassAnalysis
from .analytics_filter import AnalyticsFilter

class AnalyticsConfiguration(BaseModel):
    """
    Specifies the configuration and any analyses for the analytics filter of an Amazon S3 bucket.

    Attributes
    ----------
    Id : str
        The ID that identifies the analytics configuration.
    StorageClassAnalysis : StorageClassAnalysis
        Contains data related to access patterns to be collected and analyzed.
    Filter : Optional[AnalyticsFilter]
        The filter used to describe a set of objects for analyses.
    """
    Id: str
    StorageClassAnalysis: StorageClassAnalysis
    Filter: Optional[AnalyticsFilter] = None