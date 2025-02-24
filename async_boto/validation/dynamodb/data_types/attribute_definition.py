from pydantic import BaseModel, Field
from typing import Literal

class AttributeDefinition(BaseModel):
    AttributeName: str = Field(..., min_length=1, max_length=255)
    AttributeType: Literal["S", "N", "B"]