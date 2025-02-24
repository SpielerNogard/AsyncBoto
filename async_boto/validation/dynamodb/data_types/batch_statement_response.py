from pydantic import BaseModel, Field
from typing import Optional
from .batch_statement_error import BatchStatementError
from .attribute_value import AttributeValueDict


class BatchStatementResponse(BaseModel):
    """
    A PartiQL batch statement response.

    Attributes
    ----------
    Error : Optional[BatchStatementError]
        The error associated with a failed PartiQL batch statement.
    Item : Optional[AttributeValueDict]
        A DynamoDB item associated with a BatchStatementResponse. Maximum length of 65535.
    TableName : Optional[str]
        The table name associated with a failed PartiQL batch statement. Minimum length of 3. Maximum length of 255.
        Pattern: [a-zA-Z0-9_.-]+
    """

    Error: Optional[BatchStatementError] = None
    Item: Optional[AttributeValueDict] = None
    TableName: Optional[str] = Field(
        None, min_length=3, max_length=255, pattern=r"[a-zA-Z0-9_.-]+"
    )
