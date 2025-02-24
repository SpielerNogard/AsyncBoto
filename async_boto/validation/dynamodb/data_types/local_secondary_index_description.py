from pydantic import BaseModel, constr, conlist
from typing import List, Optional
from .key_schema_element import KeySchemaElement
from .projection import Projection as ProjectionModel


class LocalSecondaryIndexDescription(BaseModel):
    """
    Represents the properties of a local secondary index.

    Attributes
    ----------
    IndexArn : Optional[str]
        The Amazon Resource Name (ARN) that uniquely identifies the index.
    IndexName : Optional[str]
        Represents the name of the local secondary index.
    IndexSizeBytes : Optional[int]
        The total size of the specified index, in bytes.
    ItemCount : Optional[int]
        The number of items in the specified index.
    KeySchema : Optional[List[KeySchemaElement]]
        The complete key schema for the local secondary index.
    Projection : Optional[ProjectionModel]
        Represents attributes that are copied (projected) from the table into the global secondary index.
    """

    IndexArn: Optional[str] = None
    IndexName: Optional[
        constr(min_length=3, max_length=255, pattern=r"[a-zA-Z0-9_.-]+")
    ] = None
    IndexSizeBytes: Optional[int] = None
    ItemCount: Optional[int] = None
    KeySchema: Optional[conlist(KeySchemaElement, min_length=1, max_length=2)] = None
    Projection: Optional[ProjectionModel] = None
