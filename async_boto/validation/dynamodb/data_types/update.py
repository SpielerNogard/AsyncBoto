from pydantic import BaseModel, constr
from typing import Dict, Optional, Union, Literal
from .attribute_value import AttributeValue, AttributeValueDict

class Update(BaseModel):
    """
    Represents a request to perform an UpdateItem operation.

    Attributes
    ----------
    Key : AttributeValueDict
        The primary key of the item to be updated. Each element consists of an attribute name and a value for that attribute.
    TableName : constr(min_length=1, max_length=1024)
        Name of the table for the UpdateItem request. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.
    UpdateExpression : str
        An expression that defines one or more attributes to be updated, the action to be performed on them, and new value(s) for them.
    ConditionExpression : Optional[str]
        A condition that must be satisfied in order for a conditional update to succeed.
    ExpressionAttributeNames : Optional[Dict[str, str]]
        One or more substitution tokens for attribute names in an expression.
    ExpressionAttributeValues : Optional[AttributeValueDict]
        One or more values that can be substituted in an expression.
    ReturnValuesOnConditionCheckFailure : Optional[Literal['ALL_OLD', 'NONE']]
        Use ReturnValuesOnConditionCheckFailure to get the item attributes if the Update condition fails.
    """

    Key: AttributeValueDict
    TableName: constr(min_length=1, max_length=1024)
    UpdateExpression: str
    ConditionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None
    ExpressionAttributeValues: Optional[AttributeValueDict] = None
    ReturnValuesOnConditionCheckFailure: Optional[Literal['ALL_OLD', 'NONE']] = None