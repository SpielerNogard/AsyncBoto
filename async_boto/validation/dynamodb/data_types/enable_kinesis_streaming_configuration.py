from pydantic import BaseModel
from typing_extensions import Literal, Optional

class EnableKinesisStreamingConfiguration(BaseModel):
    """
    Enables setting the configuration for Kinesis Streaming.

    Attributes
    ----------
    ApproximateCreationDateTimePrecision : Literal["MILLISECOND", "MICROSECOND"], optional
        Toggle for the precision of Kinesis data stream timestamp. The values are either MILLISECOND or MICROSECOND.
    """
    ApproximateCreationDateTimePrecision: Optional[Literal["MILLISECOND", "MICROSECOND"]] = None