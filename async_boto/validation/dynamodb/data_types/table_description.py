from pydantic import BaseModel, constr
from typing import List, Optional, Literal
from datetime import datetime
from .archival_summary import ArchivalSummary as ArchivalSummaryModel
from .attribute_definition import AttributeDefinition
from .billing_mode_summary import BillingModeSummary as BillingModeSummaryModel
from .global_secondary_index_description import GlobalSecondaryIndexDescription
from .key_schema_element import KeySchemaElement
from .local_secondary_index_description import LocalSecondaryIndexDescription
from .on_demand_throughput import OnDemandThroughput as OnDemandThroughputModel
from .provisioned_throughput_description import ProvisionedThroughputDescription
from .replica_description import ReplicaDescription
from .restore_summary import RestoreSummary as RestoreSummaryModel
from .sse_description import SSEDescription as SSEDescriptionModel
from .stream_specification import StreamSpecification
from .table_class_summary import TableClassSummary as TableClassSummaryModel
from .table_warm_throughput_description import TableWarmThroughputDescription


class TableDescription(BaseModel):
    """
    Represents the properties of a table.

    Attributes
    ----------
    ArchivalSummary : Optional[ArchivalSummary]
        Contains information about the table archive.
    AttributeDefinitions : Optional[List[AttributeDefinition]]
        An array of AttributeDefinition objects.
    BillingModeSummary : Optional[BillingModeSummary]
        Contains the details for the read/write capacity mode.
    CreationDateTime : Optional[datetime]
        The date and time when the table was created, in UNIX epoch time format.
    DeletionProtectionEnabled : Optional[bool]
        Indicates whether deletion protection is enabled (true) or disabled (false) on the table.
    GlobalSecondaryIndexes : Optional[List[GlobalSecondaryIndexDescription]]
        The global secondary indexes, if any, on the table.
    GlobalTableVersion : Optional[str]
        Represents the version of global tables in use, if the table is replicated across AWS Regions.
    ItemCount : Optional[int]
        The number of items in the specified table.
    KeySchema : Optional[List[KeySchemaElement]]
        The primary key structure for the table.
    LatestStreamArn : Optional[constr(min_length=37, max_length=1024)]
        The Amazon Resource Name (ARN) that uniquely identifies the latest stream for this table.
    LatestStreamLabel : Optional[str]
        A timestamp, in ISO 8601 format, for this stream.
    LocalSecondaryIndexes : Optional[List[LocalSecondaryIndexDescription]]
        Represents one or more local secondary indexes on the table.
    MultiRegionConsistency : Optional[Literal['EVENTUAL', 'STRONG']]
        Indicates one of the following consistency modes for a global table.
    OnDemandThroughput : Optional[OnDemandThroughput]
        The maximum number of read and write units for the specified on-demand table.
    ProvisionedThroughput : Optional[ProvisionedThroughputDescription]
        The provisioned throughput settings for the table.
    Replicas : Optional[List[ReplicaDescription]]
        Represents replicas of the table.
    RestoreSummary : Optional[RestoreSummary]
        Contains details for the restore.
    SSEDescription : Optional[SSEDescription]
        The description of the server-side encryption status on the specified table.
    StreamSpecification : Optional[StreamSpecification]
        The current DynamoDB Streams configuration for the table.
    TableArn : Optional[str]
        The Amazon Resource Name (ARN) that uniquely identifies the table.
    TableClassSummary : Optional[TableClassSummary]
        Contains details of the table class.
    TableId : Optional[constr(regex=r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")]
        Unique identifier for the table for which the backup was created.
    TableName : Optional[constr(min_length=3, max_length=255, regex=r"^[a-zA-Z0-9_.-]+$")]
        The name of the table.
    TableSizeBytes : Optional[int]
        The total size of the specified table, in bytes.
    TableStatus : Optional[Literal['CREATING', 'UPDATING', 'DELETING', 'ACTIVE', 'INACCESSIBLE_ENCRYPTION_CREDENTIALS', 'ARCHIVING', 'ARCHIVED']]
        The current state of the table.
    WarmThroughput : Optional[TableWarmThroughputDescription]
        Describes the warm throughput value of the base table.
    """

    ArchivalSummary: Optional[ArchivalSummaryModel] = None
    AttributeDefinitions: Optional[List[AttributeDefinition]] = None
    BillingModeSummary: Optional[BillingModeSummaryModel] = None
    CreationDateTime: Optional[datetime] = None
    DeletionProtectionEnabled: Optional[bool] = None
    GlobalSecondaryIndexes: Optional[List[GlobalSecondaryIndexDescription]] = None
    GlobalTableVersion: Optional[str] = None
    ItemCount: Optional[int] = None
    KeySchema: Optional[List[KeySchemaElement]] = None
    LatestStreamArn: Optional[constr(min_length=37, max_length=1024)] = None
    LatestStreamLabel: Optional[str] = None
    LocalSecondaryIndexes: Optional[List[LocalSecondaryIndexDescription]] = None
    MultiRegionConsistency: Optional[Literal["EVENTUAL", "STRONG"]] = None
    OnDemandThroughput: Optional[OnDemandThroughputModel] = None
    ProvisionedThroughput: Optional[ProvisionedThroughputDescription] = None
    Replicas: Optional[List[ReplicaDescription]] = None
    RestoreSummary: Optional[RestoreSummaryModel] = None
    SSEDescription: Optional[SSEDescriptionModel] = None
    StreamSpecification: Optional[StreamSpecification] = None
    TableArn: Optional[str] = None
    TableClassSummary: Optional[TableClassSummaryModel] = None
    TableId: Optional[
        constr(
            pattern=r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
        )
    ] = None
    TableName: Optional[
        constr(min_length=3, max_length=255, pattern=r"^[a-zA-Z0-9_.-]+$")
    ] = None
    TableSizeBytes: Optional[int] = None
    TableStatus: Optional[
        Literal[
            "CREATING",
            "UPDATING",
            "DELETING",
            "ACTIVE",
            "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
            "ARCHIVING",
            "ARCHIVED",
        ]
    ] = None
    WarmThroughput: Optional[TableWarmThroughputDescription] = None
