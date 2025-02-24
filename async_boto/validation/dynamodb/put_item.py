from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Literal

from .data_types.attribute_value import AttributeValueDict, AttributeValue
from .data_types.consumed_capacity import ConsumedCapacity
from .data_types.item_collection_metrics import ItemCollectionMetrics
from .data_types.expected_attribute_value import ExpectedAttributeValue


class PutItemRequest(BaseModel):
    Item: AttributeValueDict
    TableName: str = Field(..., min_length=1, max_length=1024)
    ConditionalOperator: Optional[Literal["AND", "OR"]] = None
    ConditionExpression: Optional[str] = None
    Expected: Optional[Dict[str, ExpectedAttributeValue]] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None
    ExpressionAttributeValues: Optional[AttributeValueDict] = None
    ReturnConsumedCapacity: Optional[Literal["INDEXES", "TOTAL", "NONE"]] = None
    ReturnItemCollectionMetrics: Optional[Literal["SIZE", "NONE"]] = None
    ReturnValues: Optional[
        Literal["NONE", "ALL_OLD", "UPDATED_OLD", "ALL_NEW", "UPDATED_NEW"]
    ] = None
    ReturnValuesOnConditionCheckFailure: Optional[Literal["ALL_OLD", "NONE"]] = None

    @classmethod
    def from_python_dict(cls, data: dict, **kwargs):
        return cls(Item=AttributeValueDict.from_python_dict(data),**kwargs)

class PutItemResponse(BaseModel):
    Attributes: Optional[AttributeValueDict] = None
    ConsumedCapacity: Optional[ConsumedCapacity] = None
    ItemCollectionMetrics: Optional[ItemCollectionMetrics] = None
