from pydantic import BaseModel, constr
from typing import List, Optional, Literal
from datetime import datetime
from .key_schema_element import KeySchemaElement
from .provisioned_throughput import ProvisionedThroughput as ProvisionedThroughputModel
from .on_demand_throughput import OnDemandThroughput as OnDemandThroughputModel


class SourceTableDetails(BaseModel):
    """
    Contains the details of the table when the backup was created.

    Attributes
    ----------
    KeySchema : List[KeySchemaElement]
        Schema of the table.
    ProvisionedThroughput : ProvisionedThroughput
        Read IOPs and Write IOPS on the table when the backup was created.
    TableCreationDateTime : datetime
        Time when the source table was created.
    TableId : str
        Unique identifier for the table for which the backup was created.
    TableName : str
        The name of the table for which the backup was created.
    BillingMode : Optional[Literal['PROVISIONED', 'PAY_PER_REQUEST']]
        Controls how you are charged for read and write throughput and how you manage capacity.
    ItemCount : Optional[int]
        Number of items in the table. Note that this is an approximate value.
    OnDemandThroughput : Optional[OnDemandThroughput]
        Sets the maximum number of read and write units for the specified on-demand table.
    TableArn : Optional[constr(min_length=1, max_length=1024)]
        ARN of the table for which backup was created.
    TableSizeBytes : Optional[int]
        Size of the table in bytes. Note that this is an approximate value.
    """

    KeySchema: List[KeySchemaElement]
    ProvisionedThroughput: ProvisionedThroughputModel
    TableCreationDateTime: datetime
    TableId: constr(
        pattern=r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
    )
    TableName: constr(min_length=3, max_length=255, pattern=r"^[a-zA-Z0-9_.-]+$")
    BillingMode: Optional[Literal["PROVISIONED", "PAY_PER_REQUEST"]] = None
    ItemCount: Optional[int] = None
    OnDemandThroughput: Optional[OnDemandThroughputModel] = None
    TableArn: Optional[constr(min_length=1, max_length=1024)] = None
    TableSizeBytes: Optional[int] = None
