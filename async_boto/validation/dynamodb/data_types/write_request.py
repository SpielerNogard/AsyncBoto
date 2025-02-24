from pydantic import BaseModel
from typing import Optional, Union
from .delete_request import DeleteRequest as DeleteRequestModel
from .put_request import PutRequest as PutRequestModel


class WriteRequest(BaseModel):
    """
    Represents an operation to perform - either DeleteItem or PutItem. You can only request one of these operations, not both, in a single WriteRequest.

    Attributes
    ----------
    DeleteRequest : Optional[DeleteRequest]
        A request to perform a DeleteItem operation.
    PutRequest : Optional[PutRequest]
        A request to perform a PutItem operation.
    """

    DeleteRequest: Optional[DeleteRequestModel] = None
    PutRequest: Optional[PutRequestModel] = None

    @classmethod
    def from_item(cls, item:DeleteRequest|PutRequestModel):
        if isinstance(item, DeleteRequestModel):
            return cls(DeleteRequest=item)
        else:
            return cls(PutRequest=item)