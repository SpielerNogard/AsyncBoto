from pydantic import BaseModel

from .s3_key_filter import S3KeyFilter


class NotificationConfigurationFilter(BaseModel):
    """
    Specifies object key name filtering rules.

    Attributes
    ----------
    Key : Optional[S3KeyFilter]
        A container for object key name prefix and suffix filtering rules.
    """

    Key: S3KeyFilter | None = None
