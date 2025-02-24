from pydantic import BaseModel, constr, conlist
from typing import List, Optional, Literal
from .attribute_value import AttributeValue

class ParameterizedStatement(BaseModel):
    """
    Represents a PartiQL statement that uses parameters.

    Attributes
    ----------
    Statement : str
        A PartiQL statement that uses parameters.
    Parameters : Optional[List[AttributeValue]]
        The parameter values.
    ReturnValuesOnConditionCheckFailure : Optional[str]
        An optional parameter that returns the item attributes for a PartiQL ParameterizedStatement operation that failed a condition check.
    """

    Statement: constr(min_length=1, max_length=8192)
    Parameters: Optional[conlist(AttributeValue, min_length=1)] = None
    ReturnValuesOnConditionCheckFailure: Optional[Literal['ALL_OLD', 'NONE']] = None