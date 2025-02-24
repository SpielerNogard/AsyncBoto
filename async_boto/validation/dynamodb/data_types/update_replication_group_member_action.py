from pydantic import BaseModel, constr
from typing import List, Optional, Literal
from .replica_global_secondary_index import ReplicaGlobalSecondaryIndex
from .on_demand_throughput_override import (
    OnDemandThroughputOverride as OnDemandThroughputOverrideModel,
)
from .provisioned_throughput_override import (
    ProvisionedThroughputOverride as ProvisionedThroughputOverrideModel,
)


class UpdateReplicationGroupMemberAction(BaseModel):
    """
    Represents a replica to be modified.

    Attributes
    ----------
    RegionName : str
        The Region where the replica exists.
    GlobalSecondaryIndexes : Optional[List[ReplicaGlobalSecondaryIndex]]
        Replica-specific global secondary index settings.
    KMSMasterKeyId : Optional[str]
        The AWS KMS key of the replica that should be used for AWS KMS encryption.
    OnDemandThroughputOverride : Optional[OnDemandThroughputOverride]
        Overrides the maximum on-demand throughput for the replica table.
    ProvisionedThroughputOverride : Optional[ProvisionedThroughputOverride]
        Replica-specific provisioned throughput.
    TableClassOverride : Optional[Literal['STANDARD', 'STANDARD_INFREQUENT_ACCESS']]
        Replica-specific table class.
    """

    RegionName: str
    GlobalSecondaryIndexes: Optional[List[ReplicaGlobalSecondaryIndex]] = None
    KMSMasterKeyId: Optional[str] = None
    OnDemandThroughputOverride: Optional[OnDemandThroughputOverrideModel] = None
    ProvisionedThroughputOverride: Optional[ProvisionedThroughputOverrideModel] = None
    TableClassOverride: Optional[
        Literal["STANDARD", "STANDARD_INFREQUENT_ACCESS"]
    ] = None
