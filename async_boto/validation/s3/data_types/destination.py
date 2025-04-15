from typing import Literal

from pydantic import BaseModel

from .access_control_translation import AccessControlTranslation
from .encryption_configuration import EncryptionConfiguration
from .metrics import Metrics
from .replication_time import ReplicationTime


class Destination(BaseModel):
    """
    Specifies information about where to publish analysis or configuration results
    for an Amazon S3 bucket and S3 Replication Time Control (S3 RTC).

    Attributes
    ----------
    Bucket : str
        The Amazon Resource Name (ARN) of the bucket where results are stored.
    AccessControlTranslation : Optional[AccessControlTranslation]
        Used in cross-account scenarios to change replica ownership.
    Account : Optional[str]
        Destination bucket owner account ID in cross-account scenarios.
    EncryptionConfiguration : Optional[EncryptionConfiguration]
        Information about encryption for the destination bucket.
    Metrics : Optional[Metrics]
        Replication metrics-related settings.
    ReplicationTime : Optional[ReplicationTime]
        S3 Replication Time Control (S3 RTC) settings.
    StorageClass : Optional[Literal["STANDARD", "REDUCED_REDUNDANCY", "STANDARD_IA",
                                    "ONEZONE_IA", "INTELLIGENT_TIERING", "GLACIER",
                                    "DEEP_ARCHIVE", "OUTPOSTS", "GLACIER_IR",
                                    "SNOW", "EXPRESS_ONEZONE"]]
        The storage class to use when replicating objects.
    """

    Bucket: str
    AccessControlTranslation: AccessControlTranslation | None = None
    Account: str | None = None
    EncryptionConfiguration: EncryptionConfiguration | None = None
    Metrics: Metrics | None = None
    ReplicationTime: ReplicationTime | None = None
    StorageClass: (
        Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
            "OUTPOSTS",
            "GLACIER_IR",
            "SNOW",
            "EXPRESS_ONEZONE",
        ]
        | None
    ) = None
