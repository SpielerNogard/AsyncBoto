from pydantic import BaseModel, conlist
from typing import Dict, List, Optional
from .attribute_value import AttributeValue, AttributeValueDict


class ItemCollectionMetrics(BaseModel):
    """
    Information about item collections, if any, that were affected by the operation.

    Attributes
    ----------
    ItemCollectionKey : Optional[Dict[str, AttributeValue]]
        The partition key value of the item collection.
    SizeEstimateRangeGB : Optional[List[float]]
        An estimate of item collection size, in gigabytes.
    """

    ItemCollectionKey: Optional[AttributeValueDict] = None
    SizeEstimateRangeGB: Optional[conlist(float, min_length=2, max_length=2)] = None
