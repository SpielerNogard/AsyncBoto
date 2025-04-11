from pydantic import BaseModel
from typing import List, Literal, Optional
from .tiering import Tiering
from .intelligent_tiering_filter import IntelligentTieringFilter

class IntelligentTieringConfiguration(BaseModel):
    """
    Specifies the S3 Intelligent-Tiering configuration for an Amazon S3 bucket.

    Attributes
    ----------
    Id : str
        The ID used to identify the S3 Intelligent-Tiering configuration.
    Status : Literal["Enabled", "Disabled"]
        Specifies the status of the configuration.
    Tierings : List[Tiering]
        Specifies the S3 Intelligent-Tiering storage class tier of the configuration.
    Filter : Optional[IntelligentTieringFilter]
        Specifies a bucket filter. The configuration only includes objects that meet the filter's criteria.
    """
    Id: str
    Status: Literal["Enabled", "Disabled"]
    Tierings: List[Tiering]
    Filter: Optional[IntelligentTieringFilter]