from pydantic import BaseModel, constr
from typing import List, Optional
from .key_schema_element import KeySchemaElement
from .projection import Projection as ProjectionModel
from .on_demand_throughput import OnDemandThroughput as OnDemandThroughputModel
from .provisioned_throughput import ProvisionedThroughput as ProvisionedThroughputModel


class GlobalSecondaryIndexInfo(BaseModel):
    """
    Represents the properties of a global secondary index for the table when the backup was created.

    Attributes
    ----------
    IndexName : Optional[constr(min_length=3, max_length=255, regex=r'[a-zA-Z0-9_.-]+')]
        The name of the global secondary index.
    KeySchema : Optional[List[KeySchemaElement]]
        The complete key schema for a global secondary index.
    OnDemandThroughput : Optional[OnDemandThroughput]
        Sets the maximum number of read and write units for the specified on-demand table.
    Projection : Optional[Projection]
        Represents attributes that are copied (projected) from the table into the global secondary index.
    ProvisionedThroughput : Optional[ProvisionedThroughput]
        Represents the provisioned throughput settings for the specified global secondary index.
    """

    IndexName: Optional[
        constr(min_length=3, max_length=255, pattern=r"[a-zA-Z0-9_.-]+")
    ] = None
    KeySchema: Optional[List[KeySchemaElement]] = None
    OnDemandThroughput: Optional[OnDemandThroughputModel] = None
    Projection: Optional[ProjectionModel] = None
    ProvisionedThroughput: Optional[ProvisionedThroughputModel] = None
