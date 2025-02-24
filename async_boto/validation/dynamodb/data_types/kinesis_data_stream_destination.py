from pydantic import BaseModel, constr
from typing import Literal, Optional


class KinesisDataStreamDestination(BaseModel):
    """
    Describes a Kinesis data stream destination.

    Attributes
    ----------
    ApproximateCreationDateTimePrecision : Optional[Literal['MILLISECOND', 'MICROSECOND']]
        The precision of the Kinesis data stream timestamp.
    DestinationStatus : Optional[Literal['ENABLING', 'ACTIVE', 'DISABLING', 'DISABLED', 'ENABLE_FAILED', 'UPDATING']]
        The current status of replication.
    DestinationStatusDescription : Optional[str]
        The human-readable string that corresponds to the replica status.
    StreamArn : Optional[constr(min_length=37, max_length=1024)]
        The ARN for a specific Kinesis data stream.
    """

    ApproximateCreationDateTimePrecision: Optional[
        Literal["MILLISECOND", "MICROSECOND"]
    ] = None
    DestinationStatus: Optional[
        Literal[
            "ENABLING", "ACTIVE", "DISABLING", "DISABLED", "ENABLE_FAILED", "UPDATING"
        ]
    ] = None
    DestinationStatusDescription: Optional[str] = None
    StreamArn: Optional[constr(min_length=37, max_length=1024)] = None
