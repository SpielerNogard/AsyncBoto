from pydantic import BaseModel
from typing import Optional, Literal
from .glacier_job_parameters import GlacierJobParameters  # Assuming this is defined in a separate file
from .output_location import OutputLocation  # Assuming this is defined in a separate file
from .select_parameters import SelectParameters  # Assuming this is defined in a separate file

class RestoreRequest(BaseModel):
    """
    Container for restore job parameters.

    Attributes
    ----------
    Days : Optional[int]
        Lifetime of the active copy in days. Do not use with restores that specify OutputLocation.
    Description : Optional[str]
        The optional description for the job.
    GlacierJobParameters : Optional[GlacierJobParameters]
        S3 Glacier related parameters pertaining to this job. Do not use with restores that specify OutputLocation.
    OutputLocation : Optional[OutputLocation]
        Describes the location where the restore job's output is stored.
    SelectParameters : Optional[SelectParameters]
        Describes the parameters for Select job types.
    Tier : Optional[Literal["Standard", "Bulk", "Expedited"]]
        Retrieval tier at which the restore will be processed.
    Type : Optional[Literal["SELECT"]]
        Type of restore request.
    """
    Days: Optional[int]
    Description: Optional[str]
    GlacierJobParameters: Optional[GlacierJobParameters]
    OutputLocation: Optional[OutputLocation]
    SelectParameters: Optional[SelectParameters]
    Tier: Optional[Literal["Standard", "Bulk", "Expedited"]]
    Type: Optional[Literal["SELECT"]]