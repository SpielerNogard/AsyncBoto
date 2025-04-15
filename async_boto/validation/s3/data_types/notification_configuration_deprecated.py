from pydantic import BaseModel

from .cloud_function_configuration import CloudFunctionConfiguration
from .queue_configuration_deprecated import QueueConfigurationDeprecated
from .topic_configuration_deprecated import TopicConfigurationDeprecated


class NotificationConfigurationDeprecated(BaseModel):
    """
    A container for specifying the deprecated notification configuration of the bucket.

    Attributes
    ----------
    CloudFunctionConfiguration : Optional[CloudFunctionConfiguration]
        Container for specifying the AWS Lambda notification configuration.
    QueueConfiguration : Optional[QueueConfigurationDeprecated]
        Deprecated. Specifies the configuration for publishing messages to an
        Amazon SQS queue.
    TopicConfiguration : Optional[TopicConfigurationDeprecated]
        Deprecated. Specifies the configuration for publishing messages to an
        Amazon SNS topic.
    """

    CloudFunctionConfiguration: CloudFunctionConfiguration | None = None
    QueueConfiguration: QueueConfigurationDeprecated | None = None
    TopicConfiguration: TopicConfigurationDeprecated | None = None
