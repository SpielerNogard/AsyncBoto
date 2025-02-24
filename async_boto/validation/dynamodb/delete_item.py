from pydantic import BaseModel, Field
from typing import Optional, Dict, Literal, List
from .data_types.attribute_value import AttributeValueDict, AttributeValue
from .data_types.consumed_capacity import ConsumedCapacity
from .data_types.item_collection_metrics import ItemCollectionMetrics
from .data_types.expected_attribute_value import ExpectedAttributeValue


class DeleteItemRequest(BaseModel):
    TableName: str = Field(..., min_length=1, max_length=1024)
    Key: AttributeValueDict
    ConditionalOperator: Optional[Literal["AND", "OR"]] = None
    ConditionExpression: Optional[str] = None
    Expected: Optional[Dict[str, ExpectedAttributeValue]] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None
    ExpressionAttributeValues: Optional[AttributeValueDict] = None
    ReturnConsumedCapacity: Optional[Literal["INDEXES", "TOTAL", "NONE"]] = None
    ReturnItemCollectionMetrics: Optional[Literal["SIZE", "NONE"]] = None
    ReturnValues: Optional[Literal["NONE", "ALL_OLD"]] = None
    ReturnValuesOnConditionCheckFailure: Optional[Literal["ALL_OLD", "NONE"]] = None


class DeleteItemResponse(BaseModel):
    Attributes: Optional[AttributeValueDict] = None
    ConsumedCapacity: Optional[ConsumedCapacity] = None
    ItemCollectionMetrics: Optional[ItemCollectionMetrics] = None