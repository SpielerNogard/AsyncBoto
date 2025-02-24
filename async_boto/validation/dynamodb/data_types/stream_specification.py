from pydantic import BaseModel
from typing import Literal, Optional


class StreamSpecification(BaseModel):
    """
    Represents the DynamoDB Streams configuration for a table in DynamoDB.

    Attributes
    ----------
    StreamEnabled : bool
        Indicates whether DynamoDB Streams is enabled (true) or disabled (false) on the table.
    StreamViewType : Optional[Literal['KEYS_ONLY', 'NEW_IMAGE', 'OLD_IMAGE', 'NEW_AND_OLD_IMAGES']]
        Determines what information is written to the stream for this table when an item is modified.
    """

    StreamEnabled: bool
    StreamViewType: Optional[
        Literal["KEYS_ONLY", "NEW_IMAGE", "OLD_IMAGE", "NEW_AND_OLD_IMAGES"]
    ] = None
