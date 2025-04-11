from pydantic import BaseModel
from typing import Optional
from .s3_location import S3Location

class OutputLocation(BaseModel):
    """
    Describes the location where the restore job's output is stored.

    Attributes
    ----------
    S3 : Optional[S3Location]
        Describes an S3 location that will receive the results of the restore request.
    """
    S3: Optional[S3Location] = None