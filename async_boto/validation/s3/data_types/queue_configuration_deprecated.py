from typing import Literal

from pydantic import BaseModel


class QueueConfigurationDeprecated(BaseModel):
    """
    This data type is deprecated. Use QueueConfiguration for the same purposes.
    Specifies the configuration for publishing messages to an Amazon SQS queue
    when Amazon S3 detects specified events.

    Attributes
    ----------
    Event : Optional[Literal[...]]
        The bucket event for which to send notifications (deprecated).
    Events : Optional[List[Literal[...]]]
        A collection of bucket events for which to send notifications.
    Id : Optional[str]
        An optional unique identifier for configurations in a notification
        configuration.
    Queue : Optional[str]
        The Amazon Resource Name (ARN) of the Amazon SQS queue.
    """

    Event: (
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
        | None
    ) = None
    Events: (
        list[
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
        | None
    ) = None
    Id: str | None = None
    Queue: str | None = None
