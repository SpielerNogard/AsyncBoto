from pydantic import BaseModel, constr
from typing import List, Optional
from .key_schema_element import KeySchemaElement
from .projection import Projection as ProjectionModel
from .on_demand_throughput import OnDemandThroughput as OnDemandThroughputModel
from .provisioned_throughput_description import ProvisionedThroughputDescription
from .global_secondary_index_warm_throughput_description import (
    GlobalSecondaryIndexWarmThroughputDescription,
)


class GlobalSecondaryIndexDescription(BaseModel):
    """
    Represents the properties of a global secondary index.

    Attributes
    ----------
    Backfilling : Optional[bool]
        Indicates whether the index is currently backfilling.
    IndexArn : Optional[str]
        The Amazon Resource Name (ARN) that uniquely identifies the index.
    IndexName : Optional[constr(min_length=3, max_length=255, regex=r'[a-zA-Z0-9_.-]+')]
        The name of the global secondary index.
    IndexSizeBytes : Optional[int]
        The total size of the specified index, in bytes.
    IndexStatus : Optional[str]
        The current state of the global secondary index.
    ItemCount : Optional[int]
        The number of items in the specified index.
    KeySchema : Optional[List[KeySchemaElement]]
        The complete key schema for a global secondary index.
    OnDemandThroughput : Optional[OnDemandThroughput]
        The maximum number of read and write units for the specified global secondary index.
    Projection : Optional[Projection]
        Represents attributes that are copied (projected) from the table into the global secondary index.
    ProvisionedThroughput : Optional[ProvisionedThroughputDescription]
        Represents the provisioned throughput settings for the specified global secondary index.
    WarmThroughput : Optional[GlobalSecondaryIndexWarmThroughputDescription]
        Represents the warm throughput value for the specified secondary index.
    """

    Backfilling: Optional[bool] = None
    IndexArn: Optional[str] = None
    IndexName: Optional[
        constr(min_length=3, max_length=255, pattern=r"[a-zA-Z0-9_.-]+")
    ] = None
    IndexSizeBytes: Optional[int] = None
    IndexStatus: Optional[str] = None
    ItemCount: Optional[int] = None
    KeySchema: Optional[List[KeySchemaElement]] = None
    OnDemandThroughput: Optional[OnDemandThroughputModel] = None
    Projection: Optional[ProjectionModel] = None
    ProvisionedThroughput: Optional[ProvisionedThroughputDescription] = None
    WarmThroughput: Optional[GlobalSecondaryIndexWarmThroughputDescription] = None
