from pydantic import BaseModel, constr
from typing import List, Literal, Optional
from datetime import datetime
from .replica_description import ReplicaDescription


class GlobalTableDescription(BaseModel):
    """
    Contains details about the global table.

    Attributes
    ----------
    CreationDateTime : Optional[datetime]
        The creation time of the global table.
    GlobalTableArn : Optional[str]
        The unique identifier of the global table.
    GlobalTableName : Optional[constr(min_length=3, max_length=255, regex=r'[a-zA-Z0-9_.-]+')]
        The global table name.
    GlobalTableStatus : Optional[Literal['CREATING', 'ACTIVE', 'DELETING', 'UPDATING']]
        The current state of the global table.
    ReplicationGroup : Optional[List[ReplicaDescription]]
        The Regions where the global table has replicas.
    """

    CreationDateTime: Optional[datetime] = None
    GlobalTableArn: Optional[str] = None
    GlobalTableName: Optional[
        constr(min_length=3, max_length=255, pattern=r"[a-zA-Z0-9_.-]+")
    ] = None
    GlobalTableStatus: Optional[
        Literal["CREATING", "ACTIVE", "DELETING", "UPDATING"]
    ] = None
    ReplicationGroup: Optional[List[ReplicaDescription]] = None
