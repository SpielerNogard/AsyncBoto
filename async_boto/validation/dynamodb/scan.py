from pydantic import BaseModel, Field
from typing import Optional, List, Literal, Dict

from .data_types.attribute_value import AttributeValueDict
from .data_types.consumed_capacity import ConsumedCapacity
from .data_types.condition import Condition


class ScanRequest(BaseModel):
    TableName: str = Field(..., min_length=1, max_length=1024)
    AttributesToGet: Optional[List[str]] = Field(None, max_length=65535)
    ConditionalOperator: Optional[Literal["AND", "OR"]] = None
    ConsistentRead: Optional[bool] = None
    ExclusiveStartKey: Optional[AttributeValueDict] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None
    ExpressionAttributeValues: Optional[AttributeValueDict] = None
    FilterExpression: Optional[str] = None
    IndexName: Optional[str] = Field(None, min_length=3, max_length=255)
    Limit: Optional[int] = Field(None, ge=1)
    ProjectionExpression: Optional[str] = None
    ReturnConsumedCapacity: Optional[Literal["INDEXES", "TOTAL", "NONE"]] = None
    ScanFilter: Optional[Dict[str, Condition]] = None
    Segment: Optional[int] = Field(None, ge=0, le=999999)
    Select: Optional[
        Literal[
            "ALL_ATTRIBUTES", "ALL_PROJECTED_ATTRIBUTES", "SPECIFIC_ATTRIBUTES", "COUNT"
        ]
    ] = None
    TotalSegments: Optional[int] = Field(None, ge=1, le=1000000)


class ScanResponse(BaseModel):
    ConsumedCapacity: Optional[ConsumedCapacity] = None
    Count: Optional[int] = None
    Items: Optional[List[AttributeValueDict]] = None
    LastEvaluatedKey: Optional[AttributeValueDict] = None
    ScannedCount: Optional[int] = None
