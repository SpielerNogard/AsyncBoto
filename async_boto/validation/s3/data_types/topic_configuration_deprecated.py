from pydantic import BaseModel
from typing import List, Optional, Literal

class TopicConfigurationDeprecated(BaseModel):
    """
    A container for specifying the configuration for publication of messages to an Amazon SNS topic
    when Amazon S3 detects specified events. This data type is deprecated. Use TopicConfiguration instead.

    Attributes
    ----------
    Event : Optional[Literal[...]]
        Deprecated. Bucket event for which to send notifications.
    Events : Optional[List[Literal[...]]]
        A collection of events related to objects.
    Id : Optional[str]
        An optional unique identifier for configurations.
    Topic : Optional[str]
        Amazon SNS topic to which Amazon S3 will publish a message.
    """
    Event: Optional[Literal[
        "s3:ReducedRedundancyLostObject", "s3:ObjectCreated:*", "s3:ObjectCreated:Put",
        "s3:ObjectCreated:Post", "s3:ObjectCreated:Copy", "s3:ObjectCreated:CompleteMultipartUpload",
        "s3:ObjectRemoved:*", "s3:ObjectRemoved:Delete", "s3:ObjectRemoved:DeleteMarkerCreated",
        "s3:ObjectRestore:*", "s3:ObjectRestore:Post", "s3:ObjectRestore:Completed",
        "s3:Replication:*", "s3:Replication:OperationFailedReplication",
        "s3:Replication:OperationNotTracked", "s3:Replication:OperationMissedThreshold",
        "s3:Replication:OperationReplicatedAfterThreshold", "s3:ObjectRestore:Delete",
        "s3:LifecycleTransition", "s3:IntelligentTiering", "s3:ObjectAcl:Put",
        "s3:LifecycleExpiration:*", "s3:LifecycleExpiration:Delete",
        "s3:LifecycleExpiration:DeleteMarkerCreated", "s3:ObjectTagging:*",
        "s3:ObjectTagging:Put", "s3:ObjectTagging:Delete"
    ]]
    Events: Optional[List[Literal[
        "s3:ReducedRedundancyLostObject", "s3:ObjectCreated:*", "s3:ObjectCreated:Put",
        "s3:ObjectCreated:Post", "s3:ObjectCreated:Copy", "s3:ObjectCreated:CompleteMultipartUpload",
        "s3:ObjectRemoved:*", "s3:ObjectRemoved:Delete", "s3:ObjectRemoved:DeleteMarkerCreated",
        "s3:ObjectRestore:*", "s3:ObjectRestore:Post", "s3:ObjectRestore:Completed",
        "s3:Replication:*", "s3:Replication:OperationFailedReplication",
        "s3:Replication:OperationNotTracked", "s3:Replication:OperationMissedThreshold",
        "s3:Replication:OperationReplicatedAfterThreshold", "s3:ObjectRestore:Delete",
        "s3:LifecycleTransition", "s3:IntelligentTiering", "s3:ObjectAcl:Put",
        "s3:LifecycleExpiration:*", "s3:LifecycleExpiration:Delete",
        "s3:LifecycleExpiration:DeleteMarkerCreated", "s3:ObjectTagging:*",
        "s3:ObjectTagging:Put", "s3:ObjectTagging:Delete"
    ]]]
    Id: Optional[str]
    Topic: Optional[str]