from typing import Literal

from pydantic import BaseModel

from .delete_marker_replication import (
    DeleteMarkerReplication,  # Assuming DeleteMarkerReplication is defined
)
from .destination import (
    Destination,  # Assuming Destination is defined in a separate file
)
from .existing_object_replication import (
    ExistingObjectReplication,  # Assuming ExistingObjectReplication is defined
)
from .replication_rule_filter import (
    ReplicationRuleFilter,  # Assuming ReplicationRuleFilter is defined
)
from .source_selection_criteria import (
    SourceSelectionCriteria,  # Assuming SourceSelectionCriteria is defined
)


class ReplicationRule(BaseModel):
    """
    Specifies which Amazon S3 objects to replicate and where to store the replicas.

    Attributes
    ----------
    Destination : Destination
        A container for information about the replication destination.
    Status : Literal["Enabled", "Disabled"]
        Specifies whether the rule is enabled.
    DeleteMarkerReplication : Optional[DeleteMarkerReplication]
        Specifies whether Amazon S3 replicates delete markers.
    ExistingObjectReplication : Optional[ExistingObjectReplication]
        Optional configuration to replicate existing source bucket objects.
    Filter : Optional[ReplicationRuleFilter]
        A filter that identifies the subset of objects to which the rule applies.
    ID : Optional[str]
        A unique identifier for the rule.
    Prefix : Optional[str]
        Deprecated. An object key name prefix that identifies the objects to
        which the rule applies.
    Priority : Optional[int]
        The priority of the rule.
    SourceSelectionCriteria : Optional[SourceSelectionCriteria]
        Additional filters for identifying the source objects to replicate.
    """

    Destination: Destination
    Status: Literal["Enabled", "Disabled"]
    DeleteMarkerReplication: DeleteMarkerReplication | None = None
    ExistingObjectReplication: ExistingObjectReplication | None = None
    Filter: ReplicationRuleFilter | None = None
    ID: str | None = None
    Prefix: str | None = None
    Priority: int | None = None
    SourceSelectionCriteria: SourceSelectionCriteria | None = None
