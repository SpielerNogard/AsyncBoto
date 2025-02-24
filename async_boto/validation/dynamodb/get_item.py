from pydantic import BaseModel, Field
from typing import Optional, Dict, List, Union, Literal

from .data_types.consumed_capacity import ConsumedCapacity
from .data_types.attribute_value import AttributeValueDict


class GetItemRequest(BaseModel):
    Key: AttributeValueDict
    TableName: str = Field(..., min_length=1, max_length=1024)
    AttributesToGet: Optional[List[str]] = None
    ConsistentRead: Optional[bool] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None
    ProjectionExpression: Optional[str] = None
    ReturnConsumedCapacity: Optional[Literal["INDEXES", "TOTAL", "NONE"]] = None


class GetItemResponse(BaseModel):
    ConsumedCapacity: Optional[ConsumedCapacity] = None
    Item: Optional[AttributeValueDict] = None
