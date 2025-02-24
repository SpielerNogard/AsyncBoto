from pydantic import BaseModel
from typing import Optional, Literal


class UpdateKinesisStreamingConfiguration(BaseModel):
    """
    Enables updating the configuration for Kinesis Streaming.

    Attributes
    ----------
    ApproximateCreationDateTimePrecision : Optional[Literal['MILLISECOND', 'MICROSECOND']]
        Enables updating the precision of Kinesis data stream timestamp.
    """

    ApproximateCreationDateTimePrecision: Optional[
        Literal["MILLISECOND", "MICROSECOND"]
    ] = None
