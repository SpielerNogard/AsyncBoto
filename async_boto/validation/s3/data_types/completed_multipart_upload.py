from pydantic import BaseModel
from typing import Optional, List
from .completed_part import CompletedPart

class CompletedMultipartUpload(BaseModel):
    """
    The container for the completed multipart upload details.

    Attributes
    ----------
    Parts : Optional[List[CompletedPart]]
        Array of CompletedPart data types. If not supplied, the service sends back an HTTP 400 response.
    """
    Parts: Optional[List[CompletedPart]] = None