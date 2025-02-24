from typing import Optional, Dict, List, Literal

from pydantic import BaseModel

from .data_types.attribute_value import AttributeValueDict
from .data_types.consumed_capacity import ConsumedCapacity
from .data_types.keys_and_attributes import KeysAndAttributes


class BatchGetItemRequest(BaseModel):
    RequestItems: Dict[str, KeysAndAttributes]
    ReturnConsumedCapacity: Optional[Literal["INDEXES", "TOTAL", "NONE"]] = None


class BatchGetItemResponse(BaseModel):
    ConsumedCapacity: Optional[List[ConsumedCapacity]] = None
    Responses: Optional[Dict[str, List[AttributeValueDict]]] = None
    UnprocessedKeys: Optional[Dict[str, KeysAndAttributes]] = None
