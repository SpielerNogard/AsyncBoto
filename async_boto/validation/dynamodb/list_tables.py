from pydantic import BaseModel, Field
from typing import Optional, List


class ListTablesRequest(BaseModel):
    ExclusiveStartTableName: Optional[str] = Field(
        None, min_length=3, max_length=255, pattern=r"[a-zA-Z0-9_.-]+"
    )
    Limit: Optional[int] = Field(None, ge=1, le=100)


class ListTablesResponse(BaseModel):
    LastEvaluatedTableName: Optional[str] = Field(
        None, min_length=3, max_length=255, pattern=r"[a-zA-Z0-9_.-]+"
    )
    TableNames: List[str] = Field(..., min_length=1, max_length=100)
