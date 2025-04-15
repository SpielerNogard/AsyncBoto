from pydantic import BaseModel

from .logging_enabled import LoggingEnabled


class BucketLoggingStatus(BaseModel):
    """
    Container for logging status information.

    Attributes
    ----------
    LoggingEnabled : Optional[LoggingEnabled]
        Describes where logs are stored and the prefix that Amazon S3 assigns to all
        log object keys for a bucket.
    """

    LoggingEnabled: LoggingEnabled | None = None
