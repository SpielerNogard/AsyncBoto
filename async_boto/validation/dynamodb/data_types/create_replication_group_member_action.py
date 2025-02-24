from pydantic import BaseModel, conlist
from typing import List, Optional
from typing_extensions import Literal
from .replica_global_secondary_index import ReplicaGlobalSecondaryIndex
from .on_demand_throughput_override import (
    OnDemandThroughputOverride as OnDemandThroughputOverrideModel,
)
from .provisioned_throughput_override import (
    ProvisionedThroughputOverride as ProvisionedThroughputOverrideModel,
)


class CreateReplicationGroupMemberAction(BaseModel):
    """
    Represents a replica to be created.

    Attributes
    ----------
    RegionName : str
        The Region where the new replica will be created.
    GlobalSecondaryIndexes : Optional[List[ReplicaGlobalSecondaryIndex]]
        Replica-specific global secondary index settings.
    KMSMasterKeyId : Optional[str]
        The AWS KMS key that should be used for AWS KMS encryption in the new replica.
    OnDemandThroughputOverride : Optional[OnDemandThroughputOverrideModel]
        The maximum on-demand throughput settings for the specified replica table being created.
    ProvisionedThroughputOverride : Optional[ProvisionedThroughputOverrideModel]
        Replica-specific provisioned throughput.
    TableClassOverride : Optional[Literal["STANDARD", "STANDARD_INFREQUENT_ACCESS"]]
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
