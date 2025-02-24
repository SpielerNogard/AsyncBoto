from typing import Optional, List, Dict, Union, Literal

from pydantic import BaseModel

from .data_types.item_collection_metrics import ItemCollectionMetrics
from .data_types.consumed_capacity import ConsumedCapacity
from .data_types.write_request import WriteRequest


class BatchWriteItemRequest(BaseModel):
    RequestItems: Dict[str, List[WriteRequest]]
    ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = "NONE"
    ReturnItemCollectionMetrics: Literal["SIZE", "NONE"] = "NONE"


class BatchWriteItemsResponse(BaseModel):
    UnprocessedItems: Dict[str, List[WriteRequest]]
    ItemCollectionMetrics: Optional[Dict[str, List[ItemCollectionMetrics]]] = None
    ConsumedCapacity: Optional[List[ConsumedCapacity]] = None
