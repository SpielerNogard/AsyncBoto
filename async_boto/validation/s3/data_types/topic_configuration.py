from typing import Literal

from pydantic import BaseModel

from .notification_configuration_filter import NotificationConfigurationFilter


class TopicConfiguration(BaseModel):
    """
    A container for specifying the configuration for publication of messages to
    an Amazon SNS topic when Amazon S3 detects specified events.

    Attributes
    ----------
    Events : List[Literal[...]]
        The Amazon S3 bucket event about which to send notifications.
    TopicArn : str
        The Amazon Resource Name (ARN) of the Amazon SNS topic.
    Filter : Optional[NotificationConfigurationFilter]
        Specifies object key name filtering rules.
    Id : Optional[str]
        An optional unique identifier for configurations.
    """

    Events: list[
        Literal[
            "s3:ReducedRedundancyLostObject",
            "s3:ObjectCreated:*",
            "s3:ObjectCreated:Put",
            "s3:ObjectCreated:Post",
            "s3:ObjectCreated:Copy",
            "s3:ObjectCreated:CompleteMultipartUpload",
            "s3:ObjectRemoved:*",
            "s3:ObjectRemoved:Delete",
            "s3:ObjectRemoved:DeleteMarkerCreated",
            "s3:ObjectRestore:*",
            "s3:ObjectRestore:Post",
            "s3:ObjectRestore:Completed",
            "s3:Replication:*",
            "s3:Replication:OperationFailedReplication",
            "s3:Replication:OperationNotTracked",
            "s3:Replication:OperationMissedThreshold",
            "s3:Replication:OperationReplicatedAfterThreshold",
            "s3:ObjectRestore:Delete",
            "s3:LifecycleTransition",
            "s3:IntelligentTiering",
            "s3:ObjectAcl:Put",
            "s3:LifecycleExpiration:*",
            "s3:LifecycleExpiration:Delete",
            "s3:LifecycleExpiration:DeleteMarkerCreated",
            "s3:ObjectTagging:*",
            "s3:ObjectTagging:Put",
            "s3:ObjectTagging:Delete",
        ]
    ]
    TopicArn: str
    Filter: NotificationConfigurationFilter | None
    Id: str | None
