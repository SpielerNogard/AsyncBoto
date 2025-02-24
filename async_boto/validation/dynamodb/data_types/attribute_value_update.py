from pydantic import BaseModel
from typing import Optional, Literal
from .attribute_value import AttributeValue

class AttributeValueUpdate(BaseModel):
    Action: Optional[Literal["ADD", "PUT", "DELETE"]] = None
    Value: Optional[AttributeValue] = None