from typing import Optional, List, Dict, Literal

from pydantic import BaseModel, Field

from .data_types.attribute_value import AttributeValueDict
from .data_types.consumed_capacity import ConsumedCapacity
from .data_types.condition import Condition


class QueryRequest(BaseModel):
    TableName: str = Field(..., min_length=1, max_length=1024)
    AttributesToGet: Optional[List[str]] = None
    ConditionalOperator: Optional[Literal["AND", "OR"]] = None
    ConsistentRead: Optional[bool] = None
    ExclusiveStartKey: Optional[AttributeValueDict] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None
    ExpressionAttributeValues: Optional[AttributeValueDict] = None
    FilterExpression: Optional[str] = None
    IndexName: Optional[str] = Field(None, min_length=3, max_length=255)
    KeyConditionExpression: Optional[str] = None
    KeyConditions: Optional[Dict[str, Condition]] = None
    Limit: Optional[int] = Field(None, ge=1)
    ProjectionExpression: Optional[str] = None
    QueryFilter: Optional[Dict[str, Condition]] = None
    ReturnConsumedCapacity: Optional[Literal["INDEXES", "TOTAL", "NONE"]] = None
    ScanIndexForward: Optional[bool] = None
    Select: Optional[
        Literal[
            "ALL_ATTRIBUTES", "ALL_PROJECTED_ATTRIBUTES", "SPECIFIC_ATTRIBUTES", "COUNT"
        ]
    ] = None


class QueryResponse(BaseModel):
    ConsumedCapacity: Optional[ConsumedCapacity] = None
    Count: Optional[int] = None
    Items: Optional[List[AttributeValueDict]] = None
    LastEvaluatedKey: Optional[AttributeValueDict] = None
    ScannedCount: Optional[int] = None
