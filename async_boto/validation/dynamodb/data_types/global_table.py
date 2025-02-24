from pydantic import BaseModel, constr
from typing import List, Optional
from .replica import Replica


class GlobalTable(BaseModel):
    """
    Represents the properties of a global table.

    Attributes
    ----------
    GlobalTableName : Optional[constr(min_length=3, max_length=255, regex=r'[a-zA-Z0-9_.-]+')]
        The global table name.
    ReplicationGroup : Optional[List[Replica]]
        The Regions where the global table has replicas.
    """

    GlobalTableName: Optional[
        constr(min_length=3, max_length=255, pattern=r"[a-zA-Z0-9_.-]+")
    ] = None
    ReplicationGroup: Optional[List[Replica]] = None
