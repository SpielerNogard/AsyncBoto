from pydantic import BaseModel
from typing import Optional

class ErrorDetails(BaseModel):
    """
    Contains error details if the CreateBucketMetadataTableConfiguration request succeeds,
    but S3 Metadata was unable to create the table.

    Attributes
    ----------
    ErrorCode : Optional[str]
        The error code indicating the type of error encountered.
    ErrorMessage : Optional[str]
        The error message providing details about the error.
    """
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None