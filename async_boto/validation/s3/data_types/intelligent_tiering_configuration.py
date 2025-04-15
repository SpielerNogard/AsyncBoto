from typing import Literal

from pydantic import BaseModel

from .intelligent_tiering_filter import IntelligentTieringFilter
from .tiering import Tiering


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
        Specifies a bucket filter. The configuration only includes objects that meet
        the filter's criteria.
    """

    Id: str
    Status: Literal["Enabled", "Disabled"]
    Tierings: list[Tiering]
    Filter: IntelligentTieringFilter | None
