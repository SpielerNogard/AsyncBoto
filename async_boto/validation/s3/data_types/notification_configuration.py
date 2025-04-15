from pydantic import BaseModel

from .event_bridge_configuration import EventBridgeConfiguration
from .lambda_function_configuration import LambdaFunctionConfiguration
from .queue_configuration import QueueConfiguration
from .topic_configuration import TopicConfiguration


class NotificationConfiguration(BaseModel):
    """
    A container for specifying the notification configuration of the bucket.
    If this element is empty, notifications are turned off for the bucket.

    Attributes
    ----------
    EventBridgeConfiguration : Optional[EventBridgeConfiguration]
        Enables delivery of events to Amazon EventBridge.
    LambdaFunctionConfigurations : Optional[List[LambdaFunctionConfiguration]]
        Describes the AWS Lambda functions to invoke and the events for which to
        invoke them.
    QueueConfigurations : Optional[List[QueueConfiguration]]
        The Amazon Simple Queue Service queues to publish messages to and the events
        for which to publish messages.
    TopicConfigurations : Optional[List[TopicConfiguration]]
        The topic to which notifications are sent and the events for which notifications
         are generated.
    """

    EventBridgeConfiguration: EventBridgeConfiguration | None = None
    LambdaFunctionConfigurations: list[LambdaFunctionConfiguration] | None = None
    QueueConfigurations: list[QueueConfiguration] | None = None
    TopicConfigurations: list[TopicConfiguration] | None = None
