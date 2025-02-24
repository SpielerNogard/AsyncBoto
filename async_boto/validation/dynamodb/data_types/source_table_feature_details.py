from pydantic import BaseModel
from typing import List, Optional
from .global_secondary_index_info import GlobalSecondaryIndexInfo
from .local_secondary_index_info import LocalSecondaryIndexInfo
from .sse_description import SSEDescription as SSEDescriptionModel
from .stream_specification import StreamSpecification as StreamSpecificationModel
from .time_to_live_description import TimeToLiveDescription as TimeToLiveDescriptionModel

class SourceTableFeatureDetails(BaseModel):
    """
    Contains the details of the features enabled on the table when the backup was created.
    For example, LSIs, GSIs, streams, TTL.

    Attributes
    ----------
    GlobalSecondaryIndexes : Optional[List[GlobalSecondaryIndexInfo]]
        Represents the GSI properties for the table when the backup was created.
    LocalSecondaryIndexes : Optional[List[LocalSecondaryIndexInfo]]
        Represents the LSI properties for the table when the backup was created.
    SSEDescription : Optional[SSEDescription]
        The description of the server-side encryption status on the table when the backup was created.
    StreamDescription : Optional[StreamSpecification]
        Stream settings on the table when the backup was created.
    TimeToLiveDescription : Optional[TimeToLiveDescription]
        Time to Live settings on the table when the backup was created.
    """

    GlobalSecondaryIndexes: Optional[List[GlobalSecondaryIndexInfo]] = None
    LocalSecondaryIndexes: Optional[List[LocalSecondaryIndexInfo]] = None
    SSEDescription: Optional[SSEDescriptionModel] = None
    StreamDescription: Optional[StreamSpecificationModel] = None
    TimeToLiveDescription: Optional[TimeToLiveDescriptionModel] = None