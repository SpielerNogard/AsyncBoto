from pydantic import BaseModel, constr
from typing import List, Optional, Literal
from .attribute_definition import AttributeDefinition
from .key_schema_element import KeySchemaElement
from .global_secondary_index import GlobalSecondaryIndex
from .on_demand_throughput import OnDemandThroughput as OnDemandThroughputModel
from .provisioned_throughput import ProvisionedThroughput as ProvisionedThroughputModel
from .sse_specification import SSESpecification as SSESpecificationModel

class TableCreationParameters(BaseModel):
    """
    The parameters for the table created as part of the import operation.

    Attributes
    ----------
    AttributeDefinitions : List[AttributeDefinition]
        The attributes of the table created as part of the import operation.
    KeySchema : List[KeySchemaElement]
        The primary key and option sort key of the table created as part of the import operation.
    TableName : constr(min_length=3, max_length=255, regex=r"^[a-zA-Z0-9_.-]+$")
        The name of the table created as part of the import operation.
    BillingMode : Optional[Literal['PROVISIONED', 'PAY_PER_REQUEST']]
        The billing mode for provisioning the table created as part of the import operation.
    GlobalSecondaryIndexes : Optional[List[GlobalSecondaryIndex]]
        The Global Secondary Indexes (GSI) of the table to be created as part of the import operation.
    OnDemandThroughput : Optional[OnDemandThroughput]
        Sets the maximum number of read and write units for the specified on-demand table.
    ProvisionedThroughput : Optional[ProvisionedThroughput]
        Represents the provisioned throughput settings for a specified table or index.
    SSESpecification : Optional[SSESpecification]
        Represents the settings used to enable server-side encryption.
    """

    AttributeDefinitions: List[AttributeDefinition]
    KeySchema: List[KeySchemaElement]
    TableName: constr(min_length=3, max_length=255, pattern=r"^[a-zA-Z0-9_.-]+$")
    BillingMode: Optional[Literal['PROVISIONED', 'PAY_PER_REQUEST']] = None
    GlobalSecondaryIndexes: Optional[List[GlobalSecondaryIndex]] = None
    OnDemandThroughput: Optional[OnDemandThroughputModel] = None
    ProvisionedThroughput: Optional[ProvisionedThroughputModel] = None
    SSESpecification: Optional[SSESpecificationModel] = None