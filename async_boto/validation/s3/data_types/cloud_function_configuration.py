from pydantic import BaseModel
from typing import Optional, List, Literal

class CloudFunctionConfiguration(BaseModel):
    """
    Container for specifying the AWS Lambda notification configuration.

    Attributes
    ----------
    CloudFunction : Optional[str]
        Lambda cloud function ARN that Amazon S3 can invoke when it detects events of the specified type.
    Event : Optional[str]
        Deprecated. The bucket event for which to send notifications.
    Events : Optional[List[Literal[
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
        Bucket events for which to send notifications.
    Id : Optional[str]
        An optional unique identifier for configurations in a notification configuration.
    InvocationRole : Optional[str]
        The role supporting the invocation of the Lambda function.
    """
    CloudFunction: Optional[str] = None
    Event: Optional[str] = None
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
    ]]] = None
    Id: Optional[str] = None
    InvocationRole: Optional[str] = None