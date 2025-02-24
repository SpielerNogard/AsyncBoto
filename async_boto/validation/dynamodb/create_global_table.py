from pydantic import BaseModel, Field, constr
from typing import List, Optional
from .data_types.replica import Replica
from .data_types.global_table_description import (
    GlobalTableDescription as GlobalTableDescriptionModel,
)
import boto3



class CreateGlobalTableRequest(BaseModel):
    """
    Creates a global table from an existing table.

    Attributes
    ----------
    GlobalTableName : str
        The global table name.
    ReplicationGroup : List[Replica]
        The Regions where the global table needs to be created.
    """

    GlobalTableName: constr(min_length=3, max_length=255, pattern=r"[a-zA-Z0-9_.-]+")
    ReplicationGroup: List[Replica]


class CreateGlobalTableResponse(BaseModel):
    """
    Response for the CreateGlobalTable operation.

    Attributes
    ----------
    GlobalTableDescription : GlobalTableDescription
        Contains the details of the global table.
    """

    GlobalTableDescription: GlobalTableDescriptionModel
