from typing import Literal

from pydantic import BaseModel

from .error_details import ErrorDetails
from .metadata_table_configuration_result import MetadataTableConfigurationResult


class GetBucketMetadataTableConfigurationResult(BaseModel):
    """
    The metadata table configuration for a general-purpose bucket.

    Attributes
    ----------
    MetadataTableConfigurationResult : MetadataTableConfigurationResult
        The metadata table configuration for a general-purpose bucket.
    Status : Literal["CREATING", "ACTIVE", "FAILED"]
        The status of the metadata table.
    Error : Optional[ErrorDetails]
        Contains error details if the metadata table creation failed.
    """

    MetadataTableConfigurationResult: MetadataTableConfigurationResult
    Status: Literal["CREATING", "ACTIVE", "FAILED"]
    Error: ErrorDetails | None
