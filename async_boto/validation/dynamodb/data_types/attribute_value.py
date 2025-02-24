from typing import List, Dict, Optional

from pydantic import BaseModel, RootModel
from async_boto.utils.dynamo_conversion import to_dynamodb_json, from_dynamodb_json


class AttributeValue(BaseModel):
    S: Optional[str] = None
    N: Optional[str] = None
    B: Optional[bytes] = None
    SS: Optional[List[str]] = None
    NS: Optional[List[str]] = None
    BS: Optional[List[bytes]] = None
    M: Optional[Dict[str, "AttributeValue"]] = None
    L: Optional[List["AttributeValue"]] = None
    NULL: Optional[bool] = None
    BOOL: Optional[bool] = None


AttributeValue.model_rebuild()


class AttributeValueDict(RootModel[Dict[str, AttributeValue]]):
    @classmethod
    def from_python_dict(cls, data: dict):
        return cls(**to_dynamodb_json(data))

    def to_python_dict(self):
        return from_dynamodb_json(
            self.model_dump(exclude_none=True, exclude_defaults=True)
        )
